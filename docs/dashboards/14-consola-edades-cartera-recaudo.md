$path = "C:\Users\sopor\Documents\ProyectosBI\superset-docs\docs\dashboards\14-consola-edades-cartera-recaudo.md"

$docCompleta = @'
# Consola 14: Edades de Cartera y Recaudo

## 1. Ficha Técnica General

| Parámetro | Detalle de Especificación |
| :--- | :--- |
| **Identificador del Tablero** | `14-consola-edades-cartera-recaudo` |
| **Módulo Hospitalario** | Gestión Financiera y Cartera |
| **Frecuencia de Actualización** | Cada 8 Horas |
| **Motor de Base de Datos** | Microsoft SQL Server |
| **Esquema Semántico** | `dbo.VW_EDADES_CARTERA_RECAUDO` |
| **Plataforma de Visualización** | Apache Superset |
| **Nivel de Granularidad** | Factura - Cuota - Tercero Pagador |

---

## 2. Propósito y Alcance

### 2.1 Propósito
Monitorear de forma integral el ciclo de exigibilidad de la cartera hospitalaria emitida, la rotación de cuentas por cobrar según rangos etarios de vencimiento, la efectividad del recaudo frente a los saldos iniciales y el impacto financiero generado por glosas definitivas, devoluciones y notas crédito.

### 2.2 Alcance
Abarca todas las facturas de venta en estado radicada, aceptada o en cobro prejudicial/jurídico frente a Entidades Promotoras de Salud (EPS), Aseguradoras SOAT, Administradoras de Riesgos Laborales (ARL), Planes Voluntarios y Particulares gestionados en el sistema Hosvital HIS. No incluye facturas anuladas ni ingresos diferidos.

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en Hosvital HIS
* `MAEEMP`: Maestro de empresas pagadoras y aseguradoras (EPS/ARL/SOAT).
* `FACMAE`: Encabezado maestro de facturación de servicios de salud.
* `CARTFAC`: Detalle y control de saldos de cartera por factura y cuota.
* `RECCAJ`: Recibos de caja y notas de crédito aplicadas a cartera.
* `GLOMAE`: Maestro de registro y conciliación de glosas hospitalarias.
* `CONTRATO`: Maestro contractual y tarifas pactadas por régimen.

### 3.2 DDL de la Vista Semántica
```sql
CREATE OR ALTER VIEW dbo.VW_EDADES_CARTERA_RECAUDO AS
SELECT 
    f.NUMFAC AS Numero_Factura,
    f.FECFAC AS Fecha_Factura,
    f.FECRAD AS Fecha_Radicacion,
    f.FECVEN AS Fecha_Vencimiento,
    DATEDIFF(DAY, f.FECVEN, GETDATE()) AS Dias_Mora,
    CASE 
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) <= 0 THEN 'Corriente'
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) BETWEEN 1 AND 30 THEN '1 a 30 Días'
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) BETWEEN 31 AND 60 THEN '31 a 60 Días'
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) BETWEEN 61 AND 90 THEN '61 a 90 Días'
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) BETWEEN 91 AND 180 THEN '91 a 180 Días'
        WHEN DATEDIFF(DAY, f.FECVEN, GETDATE()) BETWEEN 181 AND 360 THEN '181 a 360 Días'
        ELSE '> 360 Días'
    END AS Franja_Etaria,
    e.MENNIT AS NIT_Aseguradora,
    e.MENNOM AS Nombre_Aseguradora,
    e.MENTIP AS Tipo_Aseguradora,
    f.VALTOT AS Valor_Facturado,
    ISNULL(c.VLRABO, 0) AS Valor_Recaudado,
    ISNULL(g.VLRGLO, 0) AS Valor_Glosa_Definitiva,
    (f.VALTOT - ISNULL(c.VLRABO, 0) - ISNULL(g.VLRGLO, 0)) AS Saldo_Neto_Exigible,
    c.ESTADO_CARTERA AS Estado_Gestion,
    c.COD_MOTIVO_GLOSA AS Codigo_Normativo_Motivo
FROM dbo.FACMAE f WITH (NOLOCK)
INNER JOIN dbo.MAEEMP e WITH (NOLOCK) ON f.CODEMP = e.MENCOD
INNER JOIN dbo.CARTFAC c WITH (NOLOCK) ON f.NUMFAC = c.NUMFAC
LEFT JOIN (
    SELECT NUMFAC, SUM(VALGLO) AS VLRGLO 
    FROM dbo.GLOMAE WITH (NOLOCK) 
    WHERE ESTGLO = 'A' 
    GROUP BY NUMFAC
) g ON f.NUMFAC = g.NUMFAC
WHERE f.ESTADO <> 'A';
```

## 4. Reglas y Lógica de Negocio
* **Exclusión de Anulaciones:** Toda factura con estado A en FACMAE se descarta de los cálculos analíticos.

* **Cómputo de Mora:** Se calcula a partir de la fecha de vencimiento pactada (FECVEN). Si no existe fecha contractual explícita, se toman 30 días calendario posteriores a la radicación (FECRAD).

* **Saldo Exigible Real:** El valor por cobrar reconoce descuentos de abonos (VLRABO) y glosas aceptadas (VLRGLO). Los saldos negativos por anticipos se segregan contablemente.

* **Corte Etario Superior:** Toda obligación superior a 360 días se marca automáticamente como candidata para provisión de cartera y deterioro según norma contable NIIF/NIC 39.

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

**Saldo Total en Cartera:**

$$\text{Saldo Total} = \sum (\text{Valor Facturado} - \text{Recaudo} - \text{Glosa Aceptada})$$

**Saldo Vencido:**

$$\text{Saldo Vencido} = \sum \text{Saldo Neto Exigible} \quad \forall \; \text{Días Mora} > 0$$

**Índice de Efectividad de Recaudo (%):**

$$\text{Efectividad Recaudo} = \left( \frac{\sum \text{Valor Recaudado Periodo}}{\sum \text{Saldo Exigible Periodo}} \right) \times 100$$

**Días de Venta en la Calle (DSO):**

$$\text{DSO} = \left( \frac{\text{Saldo Promedio de Cartera}}{\text{Facturación Total del Periodo}} \right) \times 365$$

##6. Consultas SQL por cada Chart
### KPI 1: Resumen de Indicadores Clave
```SQL
SELECT 
    SUM(Valor_Facturado) AS Total_Facturado,
    SUM(Saldo_Neto_Exigible) AS Saldo_Total_Cartera,
    SUM(CASE WHEN Dias_Mora > 0 THEN Saldo_Neto_Exigible ELSE 0 END) AS Saldo_Vencido,
    SUM(Valor_Recaudado) AS Total_Recaudado,
    ROUND((SUM(Valor_Recaudado) / NULLIF(SUM(Valor_Facturado), 0)) * 100, 2) AS Efectividad_Recaudo_Pct
FROM dbo.VW_EDADES_CARTERA_RECAUDO;
```
### Chart 2: Distribución por Estado de Gestión
```SQL
SELECT 
    Estado_Gestion,
    COUNT(Numero_Factura) AS Total_Facturas,
    SUM(Saldo_Neto_Exigible) AS Saldo_Pendiente
FROM dbo.VW_EDADES_CARTERA_RECAUDO
GROUP BY Estado_Gestion
ORDER BY Saldo_Pendiente DESC;
```
### Chart 3: Top Aseguradoras por Saldo Pendiente
```SQL
SELECT TOP 10
    Nombre_Aseguradora,
    SUM(Saldo_Neto_Exigible) AS Saldo_Pendiente,
    SUM(CASE WHEN Dias_Mora > 90 THEN Saldo_Neto_Exigible ELSE 0 END) AS Saldo_Critico_Mayor_90D
FROM dbo.VW_EDADES_CARTERA_RECAUDO
GROUP BY Nombre_Aseguradora
ORDER BY Saldo_Pendiente DESC;
```
### Chart 4: Motivos Normativos Más Frecuentes
```SQL
SELECT TOP 10
    Codigo_Normativo_Motivo,
    COUNT(*) AS Conteo_Eventos,
    SUM(Valor_Glosa_Definitiva) AS Valor_Objetado
FROM dbo.VW_EDADES_CARTERA_RECAUDO
WHERE Codigo_Normativo_Motivo IS NOT NULL
GROUP BY Codigo_Normativo_Motivo
ORDER BY Valor_Objetado DESC;
```

## 7. Estructura de Visualizaciones y KPIs
### 7.1 Esquema de Distribución en Grilla

| Fila | Componente / Distribución Horizontal |
| :---: | :--- |
| **Cabecera** | **Filtros Globales:** Aseguradora (EPS/SOAT/ARL) \| Rango de Fechas Radicación/Vencimiento \| Sede |
| **Fila 1 (KPIs)** | `[Saldo Total Cartera]` `[Saldo Vencido Exigible]` `[Recaudo Mes Acumulado]` `[% Efectividad Recaudo]` |
| **Fila 2** | **Gráfico Principal:** Distribución de Saldo por Franja Etaria (*Corriente, 1-30, 31-60, 61-90, 91-180, 181-360, >360*) |
| **Fila 3** | **Chart 2:** Estado de Gestión (Donut) \| **Chart 3:** Top 10 Aseguradoras por Cartera (Barras Horizontales) |
| **Fila 4** | **Chart 4:** Motivos Normativos de Glosa y Mora \| **Matriz Detallada:** Auditoría Factura a Factura |

### 7.2 Detalle de Configuración por Componente

#### Tarjetas KPI de Resumen Ejecutivo
* **Tipo de Visualización:** Big Number with Trendline.
* **Métrica Principal:**
    * Saldo Total: `SUM(Saldo_Neto_Exigible)`
    * Saldo Vencido: `SUM(CASE WHEN Dias_Mora > 0 THEN Saldo_Neto_Exigible ELSE 0 END)`
    * Recaudo del Periodo: `SUM(Valor_Recaudado)`
    * Efectividad (%): `(SUM(Valor_Recaudado) / NULLIF(SUM(Valor_Facturado), 0)) * 100`
* **Línea Temporal (Trendline):** `Fecha_Factura` (agrupado por Mes).
* **Formato de Número:** Moneda `$ #,##0` para valores monetarios y `0.00%` para efectividad.

---

#### Gráfico Principal: Estratificación por Franja Etaria
* **Tipo de Visualización:** Time-series Bar Chart (Stacked / Barras Apiladas).
* **Eje X (Categoría):** `Franja_Etaria` (Orden personalizado: *Corriente, 1 a 30, 31 a 60, 61 a 90, 91 a 180, 181 a 360, > 360*).
* **Métrica (Eje Y):** `SUM(Saldo_Neto_Exigible)`.
* **Desglose (Breakdown / Serie):** `Tipo_Aseguradora` (Contributivo, Subsidiado, SOAT, ARL, Particulares).
* **Tooltip:** Mostrar porcentaje de participación sobre el total de la franja.

---

#### Chart 2: Distribución por Estado de Gestión
* **Tipo de Visualización:** Donut Chart (Gráfico de Dona).
* **Dimensión:** `Estado_Gestion`.
* **Métrica:** `COUNT(Numero_Factura)`.
* **Métrica Secundaria (Tooltip):** `SUM(Saldo_Neto_Exigible)`.
* **Configuración de Etiquetas:** Mostrar Nombre de Categoría + Porcentaje.

---

#### Chart 3: Top Aseguradoras con Mayor Saldo Pendiente
* **Tipo de Visualización:** Horizontal Bar Chart (Barras Horizontales).
* **Dimensión (Eje Y):** `Nombre_Aseguradora`.
* **Métrica (Eje X):** `SUM(Saldo_Neto_Exigible)`.
* **Ordenamiento:** Descendente por `SUM(Saldo_Neto_Exigible)`.
* **Límite de Registros (Row Limit):** 10.
* **Alerta Visual:** Barra de color diferencial para saldos con `Dias_Mora > 90`.

---

#### Chart 4: Motivos Normativos de Glosa y No Pago
* **Tipo de Visualización:** Bar Chart / Treemap.
* **Dimensión:** `Codigo_Normativo_Motivo`.
* **Métrica:** `SUM(Valor_Glosa_Definitiva)`.
* **Métrica Secundaria:** `COUNT(Numero_Factura)` (Frecuencia del motivo).
* **Filtro Aplicado:** `Codigo_Normativo_Motivo IS NOT NULL`.

---

#### Matriz Detalle: Auditoría Factura a Factura
* **Tipo de Visualización:** Table View con paginación interactiva.
* **Columnas Visibles:** `Numero_Factura`, `Nombre_Aseguradora`, `Fecha_Factura`, `Fecha_Vencimiento`, `Dias_Mora`, `Franja_Etaria`, `Valor_Facturado`, `Valor_Recaudado`, `Valor_Glosa_Definitiva`, `Saldo_Neto_Exigible`, `Estado_Gestion`.
* **Orden Predeterminado:** `Dias_Mora` en orden descendente.
* **Funcionalidad:** Búsqueda rápida por texto, ordenamiento por encabezado de columna y exportación a CSV / Excel habilitada.