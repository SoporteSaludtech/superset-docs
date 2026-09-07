# Consola Facturación y Cuentas por Emitir (WIP Post-Alta)

---

## 1. Ficha Técnica General

| Parámetro | Valor / Especificación |
| :--- | :--- |
| **Nombre del Cuadro de Mando** | Consola Facturación y Cuentas por Emitir (WIP Post-Alta) |
| **Código del Manual** | `DASH-ADM-012` |
| **Área Funcional** | Gestión Administrativa / Ciclo de Ingresos Hospitalario (*Revenue Cycle Management - RCM*) |
| **Herramienta de Visualización** | IntelliHealth|iHealth|
| **Motor de Base de Datos** | Microsoft SQL Server (Hosvital HIS) |
| **Vistas Principales** | `dbo.VW_PENDIENTE_POR_FACTURAR` / `dbo.VW_FACTURACION_EMITIDA` |
| **Frecuencia de Actualización** | Cada 15 Minutos (Caché Redis / TTL IntelliHealth: 900 s) |
| **Marco Normativo Vigente** | Ley 1438 de 2011 (Arts. 56 y 57), Decreto 4747 de 2007, Circular Única SNS |
| **Audiencia / Roles de Uso** | Gerencia Financiera, Dirección Administrativa, Jefatura de Facturación, Auditoría Concurrente y Cuentas Médicas |

---

## 2. Propósito y Alcance

### 2.1 Propósito
Garantizar la supervisión y trazabilidad continua del ciclo de ingresos de la institución mediante un modelo dual:
1. **Facturación Emitida:** Análisis de la producción formalmente liquidada, facturada y radicada ante las Entidades Administradoras de Planes de Beneficios (EAPB).
2. **Cuentas por Emitir (WIP - Work in Progress):** Monitoreo operativo de atenciones con egreso médico que continúan acumulando cargos prefacturados en la tabla temporal `TMPFAC` sin haber sido cerradas ni facturadas.

### 2.2 Alcance
* **Población Objeto:** Todos los pacientes con cargos activos en `TMPFAC` y atenciones clínicas cerradas en `INGRESOS`.
* **Segregación:** Cuentas con orden médica de salida (*Post-Egreso*) vs. Cuentas con paciente en estancia (*Abiertas*).
* **Control de Oportunidad:** Detección de cuellos de botella por piso asistencial (`MAEPAB`), aseguradora (`EMPRESs`) y tipo de atención clínica.

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en Hosvital HIS

```text
  +------------------+           +------------------+
  |      TMPFAC      |           |     INGRESOS     |
  |------------------|           |------------------|
  | TmCtvIng (FK)    |---------->| IngCsc (PK)      |
  | TFCEDU / TFTDoc  |           | MPCodP (Pabellón)|
  | TFMENi (Nit EPS) |           | MPNUMC (Cama)    |
  | Clapro (Tipo)    |           | IngFecAdm (Ing)  |
  | TFVAPU (Val Pac) |           | IngFecEgr (Egr)  |
  | TFTOTP (Val Proc)|           +------------------+
  | TFTOTS (Val Sum) |                     |
  +------------------+                     |
           |                               v
           |                     +------------------+
           |                     |      MAEPAB      |
           |                     |------------------|
           |                     | MPCodP (PK)      |
           |                     | MPNomP (Nombre)  |
           |                     +------------------+
           v
  +------------------+           +------------------+
  |      MAEEMP      |           |     EMPRESs      |
  |------------------|           |------------------|
  | MENNIT (PK)      |           | MEcntr (PK)      |
  | MEcntr (FK)      |---------->| EmpDsc (Nombre)  |
  | MENOMB (Contrato)|           +------------------+
  | mecapi (Modali.) |
  +------------------+
```

### 3.2 DDL de la Vista:

VW_PENDIENTE_POR_FACTURARSQLCREATE OR ALTER VIEW dbo.VW_PENDIENTE_POR_FACTURAR AS
```SQL
WITH ResumenTmpfac AS (
    SELECT 
        tf.TmCtvIng,
        tf.TFCEDU,
        tf.TFTDoc,
        tf.TFMENi,
        tf.Clapro,
        SUM(ISNULL(tf.TFVAPU, 0)) AS VALOR_PENDIENTE,
        SUM(ISNULL(tf.TFTOTP, 0)) AS VALOR_PROCEDIMIENTOS,
        SUM(ISNULL(tf.TFTOTS, 0)) AS VALOR_SUMINISTROS,
        COUNT(1) AS CANTIDAD_CARGOS
    FROM dbo.TMPFAC tf WITH (NOLOCK)
    GROUP BY 
        tf.TmCtvIng, 
        tf.TFCEDU, 
        tf.TFTDoc, 
        tf.TFMENi, 
        tf.Clapro
    HAVING SUM(ISNULL(tf.TFVAPU, 0)) > 0
)
SELECT 
    -- 1. Identificadores de Cuenta y Usuario
    r.TmCtvIng AS CONSECUTIVO_INGRESO,
    r.TFTDoc AS TIPO_DOC_PACIENTE,
    r.TFCEDU AS IDENTIFICACION_PACIENTE,
    p.MPnomC AS PACIENTE,   
    -- 2. Ubicación Asistencial
    i.MPCodP AS PABELLON_SERVICIO,
    ISNULL(pab.MPNomP, 'Sin Pabellón Asignado') AS NOMBRE_PABELLON,
    i.MPNUMC AS CAMA_ACTUAL,
    i.IngFecAdm AS FECHA_INGRESO,
    -- 3. Temporalidad de Egreso
    CASE 
        WHEN i.IngFecEgr = '1753-01-01 00:00:00.000' THEN NULL 
        ELSE i.IngFecEgr 
    END AS FECHA_ORDEN_SALIDA,
    -- 4. Estados y Métricas de Rezago Operativo
    CASE 
        WHEN i.IngFecEgr = '1753-01-01 00:00:00.000' OR i.IngFecEgr IS NULL THEN 'Abierta (En Estancia)'
        ELSE 'Con Orden de Salida'
    END AS ESTADO_ATENCION,
    CASE 
        WHEN i.IngFecEgr <> '1753-01-01 00:00:00.000' 
             AND i.IngFecEgr IS NOT NULL 
             AND i.IngFecEgr <= GETDATE() 
        THEN DATEDIFF(day, i.IngFecEgr, GETDATE())
        ELSE 0 
    END AS DIAS_REZAGO,
    -- 5. Semáforo Normativo Ley 1438
    CASE 
        WHEN i.IngFecEgr = '1753-01-01 00:00:00.000' OR i.IngFecEgr IS NULL THEN 'En Estancia'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 3 THEN '0 – 3 d'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 7 THEN '4 – 7 d'
        ELSE '> 7 d'
    END AS RANGO_REZAGO,
    -- 6. Estratificación Cronológica Detallada
    CASE 
        WHEN i.IngFecEgr = '1753-01-01 00:00:00.000' OR i.IngFecEgr IS NULL THEN 'En Estancia'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 2 THEN '1. 0 – 2 días'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 5 THEN '2. 3 – 5 días'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 7 THEN '3. 6 – 7 días'
        WHEN DATEDIFF(day, i.IngFecEgr, GETDATE()) <= 15 THEN '4. 8 – 15 días'
        ELSE '5. > 15 días'
    END AS RANGO_REZAGO_DETALLADO,
    -- 7. Clasificación del Servicio
    CASE r.Clapro
        WHEN '1' THEN 'Urgencias'
        WHEN '2' THEN 'Consulta Externa / Ambulatorio'
        WHEN '3' THEN 'Hospitalización'
        WHEN '4' THEN 'Recién Nacido'
        WHEN '5' THEN 'Remitido'
        ELSE 'Ambulatorio / General'
    END AS TIPO_ATENCION,
    -- 8. Entidad Responsable del Pago y Contratación
    emp.EmpDsc AS ASEGURADORA,
    me.MENOMB AS CONTRATO,
    CASE me.MEestado 
        WHEN '0' THEN 'Activo' 
        WHEN '1' THEN 'Inactivo' 
        ELSE 'Otro' 
    END AS ESTADO_CONTRATO,
    CASE me.mecapi
        WHEN 0 THEN 'Cápita'
        WHEN 1 THEN 'Evento'
        WHEN 2 THEN 'PGP'
        ELSE 'Otro'
    END AS MODALIDAD_CONTRATO,
    -- 9. Importes Económicos
    r.VALOR_PENDIENTE,
    r.VALOR_PROCEDIMIENTOS,
    r.VALOR_SUMINISTROS,
    r.CANTIDAD_CARGOS
FROM ResumenTmpfac r
INNER JOIN dbo.INGRESOS i WITH (NOLOCK) 
    ON r.TmCtvIng = i.IngCsc
LEFT JOIN dbo.CAPBAS p WITH (NOLOCK) 
    ON r.TFCEDU = p.MPCEDU AND r.TFTDoc = p.MPTDoc
LEFT JOIN dbo.MAEPAB pab WITH (NOLOCK) 
    ON i.MPCodP = pab.MPCodP
LEFT JOIN dbo.MAEEMP me WITH (NOLOCK) 
    ON r.TFMENi = me.MENNIT
LEFT JOIN dbo.EMPRESs emp WITH (NOLOCK) 
    ON me.MEcntr = emp.MEcntr;
GO
```
## 4. Reglas y Lógica de NegocioTratamiento de Fecha Centinela: En Hosvital HIS, 

* los pacientes hospitalizados que aún no tienen alta médica registran en INGRESOS.IngFecEgr el valor centinela '1753-01-01 00:00:00.000'. La vista transforma este valor en NULL y lo clasifica bajo el estado Abierta (En Estancia).

* Cálculo de Días de Rezago: Solo computa para atenciones que poseen orden de salida confirmada (IngFecEgr > 1753-01-01 y fecha válida en el pasado). 

* Para pacientes activos en cama, el rezago es estrictamente 0.Agrupación Previa en TMPFAC: TMPFAC maneja cargos a nivel de ítem individual facturable. 

* La vista consolida previamente los cargos mediante un CTE (ResumenTmpfac) agrupando por ingreso, paciente y aseguradora para evitar duplicaciones cartesianas.
**Semáforo Normativo de Liquidación (Ley 1438):**
	*    **Verde (0 a 3 días):** Intervalo legal oportuno de facturación y auditoría médica.
	*    **Amarillo (4 a 7 días):** Alerta administrativa; riesgo de vencimiento en tiempos de radicación.
	*    **Rojo (> 7 días):** Desviación crítica; cuenta bloqueada por pertinencia médica, falta de soportes, autorizaciones o inconsistencia en cargos.
	
## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

**A. Total Saldo Pendiente ($S_{total}$)**  
Consolidación monetaria absoluta de cargos sin liquidar:

$$
S_{total} = \sum_{i=1}^{n} \text{VALOR\_PENDIENTE}_i
$$

**B. Saldo en Rezago Post-Alta ($S_{rezago}$)**  
Importe de atenciones con egreso médico efectivo que aún no se radican:

$$
S_{rezago} = \sum_{i \in \text{Con Orden de Salida}} \text{VALOR\_PENDIENTE}_i
$$

**C. Rezago Operativo Promedio ($\overline{R}$)**  
Días medios transcurridos desde el alta médica institucional:

$$
\overline{R} = \frac{1}{N_{alta}} \sum_{i=1}^{N_{alta}} \left( \text{Fecha Actual} - \text{Fecha Egreso}_i \right)
$$

Donde $N_{alta}$ es el total de ingresos con estado *Con Orden de Salida*.

**D. Tasa de Cumplimiento de Oportunidad ($\%Oport$)**  
Porcentaje de atenciones dentro del margen de la Ley 1438:

$$
\%Oport = \left( \frac{\sum [ \text{DIAS\_REZAGO}_i \le 3 ]}{N_{alta}} \right) \times 100
$$

---

## 6. Consultas SQL por cada Chart

**Chart 01: KPI - Total Saldo Pendiente**
```sql
SELECT SUM(VALOR_PENDIENTE) AS "Total Saldo Pendiente"
FROM dbo.VW_PENDIENTE_POR_FACTURAR;
```
**Chart 02: KPI - Saldo con Alta Médica (Rezago)**

```sql
SELECT SUM(VALOR_PENDIENTE) AS "Saldo con Alta Medica"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
WHERE ESTADO_ATENCION = 'Con Orden de Salida';
```
**Chart 03: KPI - Cuentas por Liquidar**
```SQL
SELECT COUNT(DISTINCT CONSECUTIVO_INGRESO) AS "Cuentas por Liquidar"
FROM dbo.VW_PENDIENTE_POR_FACTURAR;
```
**Chart 04: Tacómetro - Días Promedio de Rezago Operativo**

```SQL
SELECT 
    COALESCE(AVG(CASE 
        WHEN ESTADO_ATENCION = 'Con Orden de Salida' 
        THEN CAST(DIAS_REZAGO AS FLOAT) 
        ELSE NULL 
    END), 0) AS "Rezago Operativo"
FROM dbo.VW_PENDIENTE_POR_FACTURAR;
```
**Chart 05: Distribución del Saldo por Días Post-Egreso**

```SQL
SELECT 
    RANGO_REZAGO_DETALLADO AS "Rango",
    CAST(RANGO_REZAGO_DETALLADO AS VARCHAR(50)) AS "Rango_Color",
    SUM(VALOR_PENDIENTE) AS "Saldo"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
WHERE ESTADO_ATENCION = 'Con Orden de Salida'
GROUP BY RANGO_REZAGO_DETALLADO
ORDER BY RANGO_REZAGO_DETALLADO ASC;
```
**Chart 06: Rezago Operativo y Saldo por Pabellón / Servicio**

```SQL
SELECT 
    NOMBRE_PABELLON AS "Pabellon",
    AVG(CASE WHEN ESTADO_ATENCION = 'Con Orden de Salida' THEN CAST(DIAS_REZAGO AS FLOAT) ELSE NULL END) AS "Dias_Promedio",
    SUM(VALOR_PENDIENTE) AS "Saldo_Pendiente"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
WHERE ESTADO_ATENCION = 'Con Orden de Salida'
GROUP BY NOMBRE_PABELLON
ORDER BY Dias_Promedio DESC;
```
**Chart 07: Distribución por Estado Asistencial (Dona)**

```SQL
SELECT 
    ESTADO_ATENCION AS "Estado",
    SUM(VALOR_PENDIENTE) AS "Valor"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
GROUP BY ESTADO_ATENCION;
```
**Chart 08: Top 10 Aseguradoras con Mayor Saldo Pendiente**
```SQL
SELECT TOP 10
    ASEGURADORA,
    SUM(VALOR_PENDIENTE) AS "Valor_Pendiente"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
GROUP BY ASEGURADORA
ORDER BY Valor_Pendiente DESC;
```
**Chart 09: Detalle Operativo de Auditoría de Cuentas**

```SQL
SELECT 
    CONSECUTIVO_INGRESO,
    TIPO_DOC_PACIENTE,
    IDENTIFICACION_PACIENTE,
    PACIENTE,
    ASEGURADORA,
    TIPO_ATENCION,
    NOMBRE_PABELLON,
    CAMA_ACTUAL,
    FECHA_ORDEN_SALIDA,
    DIAS_REZAGO,
    RANGO_REZAGO_DETALLADO,
    SUM(VALOR_PENDIENTE) AS "VALOR_PENDIENTE",
    SUM(VALOR_PROCEDIMIENTOS) AS "VALOR_PROCEDIMIENTOS",
    SUM(VALOR_SUMINISTROS) AS "VALOR_SUMINISTROS"
FROM dbo.VW_PENDIENTE_POR_FACTURAR
GROUP BY 
    CONSECUTIVO_INGRESO, TIPO_DOC_PACIENTE, IDENTIFICACION_PACIENTE, PACIENTE,
    ASEGURADORA, TIPO_ATENCION, NOMBRE_PABELLON, CAMA_ACTUAL, FECHA_ORDEN_SALIDA,
    DIAS_REZAGO, RANGO_REZAGO_DETALLADO
ORDER BY DIAS_REZAGO DESC;
```

## 7. Estructura de Visualizaciones y KPIs 

### 7.1 Esquema de Distribución en Grilla (Grid de 12 Columnas)

```text
+---------------------------------------------------------------------------------------------------+
| PESTAÑA: PENDIENTE POR FACTURAR (WIP POST-ALTA)                                                   |
+---------------------------------------------------------------------------------------------------+
| FILA 1: KPIs EJECUTIVOS                                                                           |
| [ Total Saldo Pendiente ] (4 col) | [ Saldo con Alta Médica ] (4 col) | [ Total Cuentas ] (4 col) |
+---------------------------------------------------------------------------------------------------+
| FILA 2: GESTIÓN OPERATIVA Y REZAGO (LEY 1438)                                                     |
| [ Convención Markdown ] (3 col)   | [ Tacómetro Rezago ] (4 col)      | [ Barras x Rango ] (5 col) |
+---------------------------------------------------------------------------------------------------+
| FILA 3: CAUSA RAÍZ ASISTENCIAL                                                                    |
| [ Rezago Operativo por Servicio / Pabellón ] (12 col)                                             |
+---------------------------------------------------------------------------------------------------+
| FILA 4: DISTRIBUCIÓN Y CONCENTRACIÓN                                                              |
| [ Dona: Estado Asistencial ] (5 col) | [ Barras Horiz: Top 10 Aseguradoras ] (7 col)               |
+---------------------------------------------------------------------------------------------------+
| FILA 5: AUDITORÍA DETALLADA                                                                       |
| [ Malla de Priorización y Trabajo Operativo de Facturación ] (12 col - Ancho completo)            |
+---------------------------------------------------------------------------------------------------+
```

---

### 7.2 Detalle de Configuración por Componente

**1. Total Saldo Pendiente**

* **Tipo:** `Big Number`
* **Grid:** 4 columnas
* **Métrica:** `SUM(VALOR_PENDIENTE)`
* **Formato Numérico:** `$,.2s`
* **Subheader:** `Saldo preliminar total en cargos (TMPFAC)`

**2. Saldo con Alta Médica**

* **Tipo:** `Big Number`
* **Grid:** 4 columnas
* **Métrica:** `SUM(CASE WHEN ESTADO_ATENCION = 'Con Orden de Salida' THEN VALOR_PENDIENTE ELSE 0 END)`
* **Formato Numérico:** `$,.2s`
* **Subheader:** `Cargos con paciente egresado (Impacto directo)`

**3. Total Cuentas por Liquidar**

* **Tipo:** `Big Number`
* **Grid:** 4 columnas
* **Métrica:** `COUNT(DISTINCT CONSECUTIVO_INGRESO)`
* **Formato Numérico:** `,d`
* **Subheader:** `Ingresos con cargos en proceso`

**4. Convención de Rezago Normativo**

* **Tipo:** `Markdown`
* **Grid:** 3 columnas
* **Contenido HTML / Markdown:**

```html
<div align="center">
<br><br>
<h3><b>Convención de Rezago</b></h3>
<span style="color: #2e7d32; font-size: 13px; font-weight: bold;">Meta: ≤ 3.0 días (Ley 1438)</span>

| Antigüedad | Estado | Acción Requerida |
| :---: | :---: | :--- |
| **0 – 3 d** | 🟢 **Óptimo** | Facturación en ciclo ordinario |
| **4 – 7 d** | 🟡 **Alerta** | Agilizar auditoría médica concurrente |
| **> 7 d** | 🔴 **Crítico** | Cuentas bloqueadas / Prioridad alta |
</div>
```

**5. Tacómetro de Rezago Promedio**

* **Tipo:** `Gauge Chart` (ECharts)
* **Grid:** 4 columnas
* **Métrica:**
  ```sql
  COALESCE(AVG(CASE WHEN ESTADO_ATENCION = 'Con Orden de Salida' THEN CAST(DIAS_REZAGO AS FLOAT) ELSE NULL END), 0)
  ```
* **Configuración Customize:**
  * **Min / Max:** `0` a `15`
  * **Interval bounds:** `3, 7, 15`
  * **Interval colors:** `3, 7, 6`
  * **Number format:** `,.1f`
  * **Value format:** `{value} días`
  * **Show progress:** Desmarcado
  * **Round cap:** Desmarcado

**6. Distribución del Saldo por Días Post-Egreso**

* **Tipo:** `Bar Chart` (ECharts)
* **Grid:** 5 columnas
* **X-Axis:** `RANGO_REZAGO_DETALLADO`
* **Dimensions (Breakdown):** `CAST(RANGO_REZAGO_DETALLADO AS VARCHAR(50))` con Label `Rango_Color`
* **Métrica:** `SUM(VALOR_PENDIENTE)`
* **Filtros del Chart:** `ESTADO_ATENCION = 'Con Orden de Salida'`
* **Configuración Customize:**
  * **Stacked:** `MARCADO (ON)`
  * **Stack Position:** `Top`
  * **Show Value:** `MARCADO (ON)`
  * **Value format:** `$,.0f`

**7. Rezago Operativo por Pabellón / Servicio**

* **Tipo:** `Bar Chart` (ECharts)
* **Grid:** 12 columnas (Ancho completo)
* **X-Axis:** `NOMBRE_PABELLON`
* **Metrics:**
  * `AVG(DIAS_REZAGO)` (Label: `Días Promedio Rezago`, Formato: `,.1f`)
  * `SUM(VALOR_PENDIENTE)` (Label: `Saldo Pendiente`, Formato: `$,.2s`)
* **Filtros del Chart:** `ESTADO_ATENCION = 'Con Orden de Salida'`
* **Configuración Customize:**
  * **Orientation:** `Horizontal`
  * **Show Value:** `MARCADO (ON)`

**8. Distribución por Estado Asistencial**

* **Tipo:** `Pie Chart` (Donut)
* **Grid:** 5 columnas
* **Dimensión:** `ESTADO_ATENCION`
* **Métrica:** `SUM(VALOR_PENDIENTE)`
* **Configuración Customize:**
  * **Outer radius:** `65%`
  * **Inner radius:** `45%`
  * **Label type:** `Category and percentage`
  * **Show Legend:** Desmarcado
  * **Number format:** `$,.2s`

**9. Top 10 Aseguradoras con Mayor Saldo Pendiente**

* **Tipo:** `Bar Chart` (ECharts)
* **Grid:** 7 columnas
* **X-Axis:** `ASEGURADORA`
* **Métrica:** `SUM(VALOR_PENDIENTE)`
* **Sort:** `SUM(VALOR_PENDIENTE)` Descendente
* **Row limit:** `10`
* **Configuración Customize:**
  * **Orientation:** `Horizontal`
  * **Show Value:** `MARCADO (ON)`
  * **Number format:** `$,.2s`

**10. Detalle Operativo de Cuentas por Liquidar**

* **Tipo:** `Table`
* **Grid:** 12 columnas (Ancho completo)
* **Dimensiones:** `CONSECUTIVO_INGRESO`, `TIPO_DOC_PACIENTE`, `IDENTIFICACION_PACIENTE`, `PACIENTE`, `ASEGURADORA`, `TIPO_ATENCION`, `NOMBRE_PABELLON`, `CAMA_ACTUAL`, `FECHA_ORDEN_SALIDA`, `DIAS_REZAGO`, `RANGO_REZAGO_DETALLADO`
* **Métricas:** `SUM(VALOR_PENDIENTE)`, `SUM(VALOR_PROCEDIMIENTOS)`, `SUM(VALOR_SUMINISTROS)`
* **Sort By:** `DIAS_REZAGO` Descendente
* **Configuración Customize:**
  * **Search box:** Marcado
  * **Page length:** `15`
  * **Table Font Size:** `small`
  * **Number format:** `$,.0f`