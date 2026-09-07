# Consola de Glosas y Devoluciones - Ficha Técnica y Manual de Operación

---

## 1. Ficha Técnica General

| Parámetro | Definición Técnica |
| :--- | :--- |
| **Nombre del Cuadro de Mando** | Consola de Glosas y Devoluciones |
| **Identificador / Slug Superset** | \consola-glosas-devoluciones\ |
| **Base de Datos Origen** | \HVT_HOSVITAL\ (Microsoft SQL Server) |
| **Objeto Principal Semántico** | \dbo.VW_GLOSAS_Y_DEVOLUCIONES\ |
| **Frecuencia de Refresco** | D-1 (Nocturno / 24 Horas) con opción de recarga manual bajo demanda |
| **Mecanismo de Consulta** | Direct Query mediante SQLAlchemy / PyODBC |
| **Audiencia Objetivo** | Dirección Financiera, Jefatura de Cartera, Auditoría Médica y Facturación |

---

## 2. Propósito y Alcance

### 2.1 Propósito
Centralizar el seguimiento del ciclo de vida de las objeciones formuladas por las Entidades Administradoras de Planes de Beneficios (EAPB / EPS), facilitando la detección de pérdidas asumidas, la gestión de saldos en litigio y la oportunidad de recobro institucional antes de su vencimiento legal.

### 2.2 Alcance
Comprende la totalidad de facturas hospitalarias emitidas en Hosvital HIS que registren al menos un evento de glosa parcial o devolución integral de cuenta médica, abarcando desde la notificación externa hasta el acta final de conciliación o cierre contable.

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en Hosvital HIS

| Tabla | Rol en el Ecosistema | Claves Primarias / Foráneas |
| :--- | :--- | :--- |
| **\ADGLOSAS\** | Cabecera maestro de la notificación | \GloNum\ (PK), \MPNFac\ (FK), \GloEdo\ |
| **\ADGLOSAS1\** | Detalle monetario por ítem objetado | \GloNum\ (PK), \GloItem\ (PK), \PRNCON\ |
| **\MAEATE\** | Maestro de atenciones y facturas | \MPNFac\ (PK), \MATipDoc\, \MPTDoc\ |
| **\GLOSAS\** | Catálogo unificado de motivos normativos | \GlsCod\ (PK) |
| **\MAEPRO\** | Maestro de procedimientos y medicamentos | \PRNCON\ (PK), \PRNCON1\ (CUPS/CUM) |
| **\MAEEMP\** | Catálogo de aseguradoras / pagadores | \MenNit\ (PK), \MenNom\ |

### 3.2 DDL de la Vista Semántica

```sql
CREATE OR ALTER VIEW dbo.VW_GLOSAS_Y_DEVOLUCIONES AS
SELECT 
    -- 1. Identificación Institucional y Factura
    CAST(g.GloNum AS VARCHAR(20))           AS CODIGO_GLOSA,
    CAST(d.GloItem AS INT)                  AS ITEM_GLOSA,
    CAST(g.MPNFac AS VARCHAR(20))           AS NUMERO_FACTURA,
    CASE 
        WHEN g.GloTip = 'D' THEN 'Devolución Total'
        ELSE 'Glosa Parcial'
    END                                     AS TIPO_OBJECION,

    -- 2. Aseguradora y Contratación
    ISNULL(e.MenNit, 'SIN_NIT')             AS NIT_ASEGURADORA,
    ISNULL(e.MenNom, 'PARTICULAR / OTRO')   AS NOMBRE_ASEGURADORA,
    
    -- 3. Normatividad y Motivo
    ISNULL(m.GlsCod, 'N/A')                 AS CODIGO_MOTIVO,
    ISNULL(m.GlsNom, 'Sin Motivo Homologado') AS DESCRIPCION_MOTIVO,
    
    -- 4. Detalle del Procedimiento / Medicamento
    ISNULL(p.PRNCON1, 'SIN_CUPS')           AS CODIGO_ITEM_CUPS,
    ISNULL(p.PRNOMB, 'Consumo No Especificado') AS DESCRIPCION_ITEM,

    -- 5. Ciclo de Vida y Estados
    CASE 
        WHEN g.GloEdo IN (1, 2) THEN 'Notificada (Sin Responder)'
        WHEN g.GloEdo IN (3, 4, 11) THEN 'Respondida / En Trámite'
        WHEN g.GloEdo IN (5, 6, 8, 9) THEN 'En Conciliación'
        WHEN g.GloEdo IN (12, 13) THEN 'Cerrada / Conciliada'
        ELSE 'En Revisión Auditoría'
    END                                     AS ESTADO_HOMOLOGADO,
    
    -- 6. Trazabilidad Temporal
    g.GloFecNot                             AS FECHA_NOTIFICACION,
    CASE 
        WHEN g.GloFecRes = '1900-01-01' THEN NULL 
        ELSE g.GloFecRes 
    END                                     AS FECHA_RESPUESTA,

    -- 7. Métricas Financieras
    CAST(d.GloVlr AS DECIMAL(18,2))         AS VALOR_GLOSADO,
    CAST(ISNULL(d.GloVlrLev, 0) AS DECIMAL(18,2)) AS VALOR_LEVANTADO,
    CAST(ISNULL(d.GloVlrAce, 0) AS DECIMAL(18,2)) AS VALOR_ACEPTADO,
    CAST(d.GloVlr - (ISNULL(d.GloVlrLev, 0) + ISNULL(d.GloVlrAce, 0)) AS DECIMAL(18,2)) AS SALDO_PENDIENTE

FROM dbo.ADGLOSAS g
INNER JOIN dbo.ADGLOSAS1 d 
    ON g.GloNum = d.GloNum
LEFT JOIN dbo.MAEATE f 
    ON g.MPNFac = f.MPNFac
LEFT JOIN dbo.MAEEMP e 
    ON f.MenNit = e.MenNit
LEFT JOIN dbo.GLOSAS m 
    ON d.GlsCod = m.GlsCod
LEFT JOIN dbo.MAEPRO p 
    ON d.PRNCON = p.PRNCON;
```

---

## 4. Reglas y Lógica de Negocio

* **Tratamiento de Fecha Centinela:** En Hosvital HIS, los campos de fecha sin diligenciar (tales como fecha de respuesta GloFecRes o fecha de conciliación) registran por convención interna el valor centinela '1900-01-01 00:00:00.000'. Para evitar sesgos en el cálculo de tiempos de respuesta en Apache Superset, se transforman explícitamente a NULL mediante sentencias CASE.
* **Criterio de Duplicidad:** La granularidad mínima analítica corresponde a la tupla (CODIGO_GLOSA, ITEM_GLOSA). No deben realizarse agregaciones directamente sobre la cabecera sin agrupar por el renglón de detalle.
* **Devoluciones Totales:** Cuando el tipo de objeción es 'D', el valor glosado inicial equivale al 100% del valor total facturado en MAEATE.

---

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

* **Valor Total Glosado:**

$$\text{VALOR\_GLOSADO} = \sum \text{GloVlr}$$
  
* **Valor Total Levantado:**

$$\text{VALOR\_LEVANTADO} = \sum \text{GloVlrLev}$$
  
* **Valor Total Aceptado (Pérdida):**

$$\text{VALOR\_ACEPTADO} = \sum \text{GloVlrAce}$$
  
* **Saldo en Disputa (Pendiente):**

  $\text{SALDO\PENDIENTE} = \text{VALOR\_GLOSADO}-(\text{VALOR\_LEVANTADO}+\text{VALOR\_ACEPTADO})$
  
* **Porcentaje de Efectividad de Recuperación:**

$$\%\text{Efectividad}=\left(\frac{\text{VALOR\LEVANTADO}}{\text{VALOR\GLOSADO}}\right)\times 100$$
  
* **Tasa de Aceptación (Pérdida Asumida):**

$$\% \text{ Pérdida} = \left(\frac{\text{VALOR\_ACEPTADO}}{\text{VALOR\_GLOSADO}}\right) \times 100$$

---

## 6. Consultas SQL por cada Chart

### KPI 1: Resumen de Indicadores Clave
```sql
SELECT 
    SUM(VALOR_GLOSADO)    AS TOTAL_GLOSADO,
    SUM(VALOR_LEVANTADO)  AS TOTAL_LEVANTADO,
    SUM(VALOR_ACEPTADO)   AS TOTAL_ACEPTADO,
    SUM(SALDO_PENDIENTE)  AS TOTAL_PENDIENTE,
    ROUND((SUM(VALOR_LEVANTADO) / NULLIF(SUM(VALOR_GLOSADO), 0)) * 100, 2) AS PCT_EFECTIVIDAD
FROM dbo.VW_GLOSAS_Y_DEVOLUCIONES
WHERE FECHA_NOTIFICACION >= :desde AND FECHA_NOTIFICACION <= :hasta;
```

### Chart 2: Distribución por Estado de Gestión
```sql
SELECT 
    ESTADO_HOMOLOGADO,
    COUNT(DISTINCT CODIGO_GLOSA) AS CANTIDAD_GLOSAS,
    SUM(SALDO_PENDIENTE)         AS SALDO_EN_DISPUTA
FROM dbo.VW_GLOSAS_Y_DEVOLUCIONES
GROUP BY ESTADO_HOMOLOGADO
ORDER BY SALDO_EN_DISPUTA DESC;
```

### Chart 3: Top Aseguradoras por Saldo Pendiente
```sql
SELECT TOP 10
    NOMBRE_ASEGURADORA,
    SUM(VALOR_GLOSADO)   AS GLOSADO,
    SUM(VALOR_LEVANTADO) AS LEVANTADO,
    SUM(SALDO_PENDIENTE) AS PENDIENTE
FROM dbo.VW_GLOSAS_Y_DEVOLUCIONES
GROUP BY NOMBRE_ASEGURADORA
ORDER BY PENDIENTE DESC;
```

### Chart 4: Motivos Normativos Más Frecuentes
```sql
SELECT TOP 10
    CODIGO_MOTIVO + ' - ' + DESCRIPCION_MOTIVO AS MOTIVO,
    COUNT(*)                                  AS FRECUENCIA_ITEMS,
    SUM(VALOR_GLOSADO)                        AS VALOR_TOTAL_GLOSADO
FROM dbo.VW_GLOSAS_Y_DEVOLUCIONES
GROUP BY CODIGO_MOTIVO, DESCRIPCION_MOTIVO
ORDER BY VALOR_TOTAL_GLOSADO DESC;
```

---

## 7. Estructura de Visualizaciones y KPIs

### 7.1 Esquema de Distribución en Grilla

```ext
+-------------------------------------------------------------------------------+
|                        FILTROS GLOBALES (Período / EPS / Estado)               |
+---------------------+-------------------+------------------+------------------+
| KPI: Total Glosado  | KPI: Vlr Levantado| KPI: Vlr Aceptado| KPI: Efectividad |
+---------------------+-------------------+------------------+------------------+
|      Barras: Saldo Pendiente por EPS    |    Dona: Distribución por Estado   |
|               (Top 10 Pagadores)        |         de Conciliación              |
+-----------------------------------------+-------------------------------------+
|        Treemap / Barras Horizontales: Principales Motivos de Glosa           |
+-------------------------------------------------------------------------------+
|         Tabla Detallada de Facturas Objetadas y Días de Vencimiento           |
+-------------------------------------------------------------------------------+
```

### 7.2 Detalle de Configuración por Componente

* **Tarjetas Numéricas (Big Number with Trendline):**
  * Cuatro KPIs superiores con formato monetario estándar en millones ($ ,.2f) y porcentaje con un decimal (.1%).
* **Gráfico de Barras Agrupadas (Top Aseguradoras):**
  * Muestra comparativa directa entre el valor objetado y el valor efectivamente levantado para evaluar el comportamiento negociador de cada EPS.
* **Gráfico Tipo Dona (Distribución de Estados):**
  * Representación porcentual del estado de la cartera en disputa, permitiendo aislar de inmediato lo que se encuentra en término de respuesta vs. lo que está en mesa de concertación.
* **Matriz Tabular Drill-Down:**
  * Vista transaccional con paginación integrada para auditoría médica operativa, listando número de factura, código CUPS, motivo y saldos.
