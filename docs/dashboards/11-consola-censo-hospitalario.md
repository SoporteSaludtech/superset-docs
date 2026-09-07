# Consola de Gestión y Censo Hospitalario

## 1. Ficha Técnica General

| Parámetro | Detalle |
| :--- | :--- |
| **Nombre del Dashboard** | Consola de Gestión y Censo Hospitalario |
| **Módulo Asistencial** | Hospitalización / Gestión de Camas (*Bed Management*) |
| **Dataset Asociado** | `DS_CENSO_HOSPITALARIO_LIVE` (Virtual Dataset) |
| **Motor de Base de Datos** | Microsoft SQL Server (Hosvital HIS) |
| **Frecuencia de Refresco** | Auto-refresh cada 5 minutos |
| **Audiencia Objetivo** | Jefaturas de Enfermería, Gestión de Camas, Auditoría Médica, Gerencia Asistencial |

---

## 2. Propósito y Alcance

La **Consola de Gestión y Censo Hospitalario** proporciona visibilidad táctica y operativa en tiempo real sobre la capacidad instalada institucional, la dotación de camas activas, la disponibilidad para asignación inmediata y el monitoreo de pacientes hospitalizados. 

Permite identificar cuellos de botella en la rotación de camas (bloqueos por desinfección o mantenimiento) y detectar oportunamente estancias hospitalarias prolongadas (>15 días y 8-15 días) para agilizar las conductas de egreso y auditoría concurrente.

---

## 3. Modelo de Datos y Origen de Información

El dataset se construye mediante una consulta virtual no bloqueante (`WITH (NOLOCK)`) cruzando las siguientes tablas transaccionales y maestras de Hosvital HIS:

* **`dbo.MAEPAB`**: Maestro institucional de pabellones y servicios (`MPCodP`, `MPNomP`).
* **`dbo.MAEPAB1`**: Maestro físico de camas institucionales (`MPCodP`, `MPNumC`, `MPDisp`, `MPActCam`, `MPCtvIn`, `MPUDoc`, `MPUced`, `MPFchI`, `MPUdx`).
* **`dbo.MAEPAB11`**: Trazabilidad histórica de movimientos de cama (`HisCamEdo`, `HisCamCtv`, `HisCamFec`, `HisCamHor`).
* **`dbo.CAPBAS`**: Maestro de identificación básica de usuarios (`MPCedu`, `MPTdoc`, nombres, fecha de nacimiento, género).
* **`dbo.INGRESOS`**: Maestro transaccional de admisiones hospitalarias (`MPCedu`, `MPTDoc`, `IngCsc`, `IngFecAdm`, `IngNit`, `IngEntDx`, `IngFecEgr`).

---

## 4. Consulta SQL del Dataset (`DS_CENSO_HOSPITALARIO_LIVE`)

```sql
WITH UltimoMovimientoCama AS (
    SELECT 
        m11.MPCodP,
        m11.MPNumC,
        m11.HisCamEdo,
        m11.HisCamFec,
        m11.HisCamHor,
        m11.HisCamCtv,
        ROW_NUMBER() OVER (
            PARTITION BY m11.MPCodP, m11.MPNumC 
            ORDER BY m11.HisCamCtv DESC
        ) AS rn
    FROM dbo.MAEPAB11 AS m11 WITH (NOLOCK)
)
SELECT 
    -- 1. Jerarquía Física y Ubicación
    p1.MPCodP AS COD_PABELLON,
    ISNULL(pab.MPNomP, CONCAT('Pabellón ', p1.MPCodP)) AS PABELLON,
    RTRIM(p1.MPNumC) AS NUMERO_CAMA,
    p1.MPActCam AS ACTIVA,

    -- 2. Estado Operativo de la Cama
    p1.MPDisp AS COD_DISPONIBILIDAD,
    CASE 
        WHEN p1.MPDisp <> '0' THEN 'Ocupada'
        WHEN ult.HisCamEdo = 'D' THEN 'En Desinfección'
        WHEN ult.HisCamEdo = 'M' THEN 'En Mantenimiento'
        WHEN ult.HisCamEdo = 'L' THEN 'Disponible / Libre'
        ELSE 'Disponible / Libre'
    END AS ESTADO_CAMA,

    -- 3. Identificación del Paciente Ocupante (CAPBAS)
    p1.MPCtvIn AS CONSECUTIVO_INGRESO,
    p1.MPUDoc AS TIPO_DOCUMENTO,
    RTRIM(p1.MPUced) AS NUMERO_DOCUMENTO,
    RTRIM(LTRIM(CONCAT(pac.MPNom1, ' ', pac.MPNom2, ' ', pac.MPApe1, ' ', pac.MPApe2))) AS NOMBRE_PACIENTE,
    pac.MPSexo AS GENERO,
    DATEDIFF(YEAR, pac.MPFchN, GETDATE()) AS EDAD_PACIENTE,

    -- 4. Métricas de Estancia y Tiempos
    p1.MPFchI AS FECHA_OCUPACION_CAMA,
    ing.IngFecAdm AS FECHA_INGRESO_INSTITUCIONAL,
    ult.HisCamFec AS FECHA_ULTIMO_MOVIMIENTO,
    CASE 
        WHEN p1.MPDisp <> 0 AND ing.IngFecAdm IS NOT NULL 
        THEN DATEDIFF(DAY, ing.IngFecAdm, GETDATE())
        WHEN p1.MPDisp <> 0 AND p1.MPFchI IS NOT NULL 
        THEN DATEDIFF(DAY, p1.MPFchI, GETDATE())
        ELSE 0 
    END AS DIAS_ESTANCIA_TOTAL,
    CASE 
        WHEN p1.MPDisp <> 0 THEN
            CASE 
                WHEN DATEDIFF(DAY, ISNULL(ing.IngFecAdm, p1.MPFchI), GETDATE()) > 15 THEN 'Prolongada (>15d)'
                WHEN DATEDIFF(DAY, ISNULL(ing.IngFecAdm, p1.MPFchI), GETDATE()) BETWEEN 8 AND 15 THEN 'Alta (8-15d)'
                WHEN DATEDIFF(DAY, ISNULL(ing.IngFecAdm, p1.MPFchI), GETDATE()) BETWEEN 3 AND 7 THEN 'Moderada (3-7d)'
                ELSE 'Corta (<=2d)'
            END
        ELSE 'Sin Ocupación'
    END AS RANGO_ESTANCIA,

    -- 5. Asegurador y Diagnóstico
    ISNULL(RTRIM(ing.IngNit), 'PARTICULAR / SIN EPS') AS ASEGURADOR_EPS,
    RTRIM(COALESCE(p1.MPUdx, ing.IngEntDx, 'SIN DIAGNOSTICO')) AS CODIGO_CIE10

FROM dbo.MAEPAB1 AS p1 WITH (NOLOCK)

-- Maestro de Pabellón
LEFT JOIN dbo.MAEPAB AS pab WITH (NOLOCK) 
    ON p1.MPCodP = pab.MPCodP

-- Último estado en la traza histórica
LEFT JOIN UltimoMovimientoCama AS ult 
    ON p1.MPCodP = ult.MPCodP 
    AND p1.MPNumC = ult.MPNumC 
    AND ult.rn = 1

-- Paciente actual en cama
LEFT JOIN dbo.CAPBAS AS pac WITH (NOLOCK) 
    ON p1.MPUced = pac.MPCedu 
    AND p1.MPUDoc = pac.MPTdoc

-- Ingreso asistencial activo
LEFT JOIN dbo.INGRESOS AS ing WITH (NOLOCK) 
    ON p1.MPUced = ing.MPCedu 
    AND p1.MPUDoc = ing.MPTDoc 
    AND p1.MPCtvIn = ing.IngCsc
    AND ing.IngFecEgr IS NULL

WHERE p1.MPActCam = 'N' OR p1.MPActCam = 'S';
```

##  5. Reglas y Lógica de Negocio

#### 5.1 Estado Físico vs. Operativo
La determinación del estado de cada cama se realiza mediante una jerarquía de dos niveles:

1. **Ocupación Activa:**  
   Se evalúa la bandera principal `MPDisp <> '0'`. Si se cumple, la cama se categoriza inmediatamente como **Ocupada**.
2. **Acondicionamiento / Disponibilidad:**  
   Si la cama no se encuentra ocupada (`MPDisp = '0'`), se consulta el registro más reciente en la traza histórica `MAEPAB11` (ordenado por `HisCamCtv DESC`) para discriminar el estado operativo:
   * **`D`**: **En Desinfección** (aseo terminal o preparación post-egreso).
   * **`M`**: **En Mantenimiento** (falla técnica, daño locativo o reparación física).
   * **`L` o por defecto**: **Disponible / Libre** (lista para asignación inmediata).

#### 5.2 Cálculo y Estratificación de Estancia
* **Días de Estancia:** Se calculan de forma prioritaria a partir de la fecha de admisión institucional (`IngFecAdm`). En ausencia de este valor, se utiliza la fecha de asignación física de la cama (`MPFchI`).
* **Rangos Clínicos de Estancia:**
  * **Corta:** $\le 2$ días.
  * **Moderada:** 3 a 7 días.
  * **Alta:** 8 a 15 días.
  * **Prolongada:** $> 15$ días.

## 6. Métricas y Lógica Aritmética de Capacidad

La consola no implementa modelos predictivos ni inferencias estadísticas complejas. Su operación se fundamenta en **álgebra de capacidad instalada, diferenciales temporales transaccionales y agregaciones condicionales** en tiempo real:

---

### 6.1 Tasa de Ocupación Global (%)
Mide la proporción porcentual de camas ocupadas frente a la dotación total física activa:

$$\text{Tasa de Ocupación (\%)} = \left( \frac{\sum \text{Camas Ocupadas}}{\sum \text{Total Camas Habilitadas}} \right) \times 100$$

* **Expresión (Custom SQL):**
```sql
ROUND((COUNT(CASE WHEN ESTADO_CAMA = 'Ocupada' THEN 1 END) * 100.0) / NULLIF(COUNT(NUMERO_CAMA), 0), 1);
```

#### 6.1.1 Semaforización Operativa y Rangos de Control

El indicador implementa una escala de semaforización visual estandarizada, orientada al monitoreo en tiempo real de la capacidad instalada y la prevención oportuna de eventos de saturación asistencial:

| Rango de Ocupación | Semáforo | Estado Operativo | Interpretación y Conducta Asistencial |
| :---: | :---: | :--- | :--- |
| **< 60%** | 🔴 Rojo | **Subocupación** | Capacidad ociosa elevada. Posible desbalance en la asignación de recursos físicos o subregistro en admisiones activas. |
| **60% – 74%** | 🟡 Amarillo | **Alerta / Capacidad baja** | Operación por debajo del umbral óptimo de eficiencia y sostenibilidad del servicio. |
| **75% – 95%** | 🟢 Verde | **Rango Óptimo** | Punto de equilibrio institucional. Flujo asistencial eficiente con margen de seguridad para contingencias y traslados. |
| **> 95%** | 🔴 Rojo | **Saturación Crítica** | Sobredemanda asistencial y riesgo de colapso en piso. Exige activación inmediata de protocolos de egreso oportuno y derivación de urgencias. |

> **Implementación en Interfaz:**  
> Para facilitar la lectura rápida del equipo asistencial, la consola integra esta escala mediante un componente visual de convenciones en la cabecera de indicadores:
> 
> `Semaforización: 🔴 < 60% Subocupación | 🟡 60% - 74% Alerta | 🟢 75% - 95% Óptimo | 🔴 > 95% Saturación Crítica`

**Nota técnica:** Se implementa NULL IF(..., 0) como salvaguarda aritmética para evitar excepciones de división por cero ante filtros que aíslen áreas sin camas asignadas.


### 6.2 Días de Estancia Hospitalaria Acumulada ($\Delta t$)
Cuantifica los días calendario transcurridos de permanencia institucional hasta el momento exacto del corte:

$$\text{Días de Estancia} = \text{Fecha Corte (Hoy)} - \text{Fecha Admisión}$$

* **Expresión (Custom SQL):**
```sql
DATEDIFF(DAY, ISNULL(ing.IngFecAdm, p1.MPFchI), GETDATE());
```
**Regla de asignación:** Prioriza la fecha de admisión institucional (IngFecAdm); en su defecto, toma la fecha de ocupación de la cama (MPFchI).

### 6.3 Edad Cronológica del Paciente
Diferencial anual para la estratificación demográfica en el censo:

$$\text{Edad} = \text{Año Actual} - \text{Año Nacimiento}$$

* **Expresión (Custom SQL):**
```
DATEDIFF(YEAR, pac.MPFchN, GETDATE());
```

### 6.4 Agregaciones Condicionales de Dotación (Censos Parciales)
Conteos booleanos aplicados para determinar el volumen por estado operativo:

**Camas Ocupadas:**

```SQL
COUNT(CASE WHEN ESTADO_CAMA = 'Ocupada' THEN 1 END);
```
**Camas Disponibles:**

```SQL
COUNT(CASE WHEN ESTADO_CAMA = 'Disponible / Libre' THEN 1 END);
```
**Camas en Acondicionamiento (Bloqueo Operativo):**

```SQL
COUNT(CASE WHEN ESTADO_CAMA IN ('En Desinfección', 'En Mantenimiento') THEN 1 END);
```

## 7. Estructura de Visualizaciones y KPIs
**Fila 1:** Indicadores Clave de Desempeño (KPIs)

**Total Camas Habilitadas:**

```SQL
COUNT(NUMERO_CAMA);
```

**Camas Ocupadas:**

```SQL
COUNT(CASE WHEN ESTADO_CAMA = 'Ocupada' THEN 1 END);
```

**Camas Disponibles:**

```SQL
COUNT(CASE WHEN ESTADO_CAMA = 'Disponible / Libre' THEN 1 END);
```

**Camas en Acondicionamiento:**

```SQL
COUNT(CASE WHEN ESTADO_CAMA IN ('En Desinfección', 'En Mantenimiento') THEN 1 END);
```


**Fila 2:** Distribución Táctica

**Tipo de Gráfico:** Horizontal Stacked Bar Chart (Distribución de Camas por Pabellón y Estado).

* **Eje Y (Categorías):** PABELLON

* **Eje X (Métrica):** COUNT(NUMERO_CAMA)

* **Serie / Desglose (Breakdown):** ESTADO_CAMA

**Fila 3:** Matriz Nominal Operativa

**Tipo de Gráfico:** Table Chart (Matriz Nominal del Censo Hospitalario).

**Columnas:**

* PABELLON

* NUMERO_CAMA

* ESTADO_CAMA

* NUMERO_DOCUMENTO

* NOMBRE_PACIENTE

* EDAD_PACIENTE

* FECHA_INGRESO_INSTITUCIONAL

* DIAS_ESTANCIA_TOTAL

* RANGO_ESTANCIA

* ASEGURADOR_EPS

* CODIGO_CIE10

**Ajustes de Interfaz:** Casilla Show Cell Bars desmarcada; buscador nativo local desactivado para centralizar la consulta en los filtros globales.

## 8. Filtros Nativos Globales (Native Filters)

**Pabellón / Servicio**

* Tipo: Value

* Columna Origen: PABELLON

* Comportamiento: Selección múltiple

* Alcance (Scoping): Todo el tablero

**Estado de Cama**

* Tipo: Value

* Columna Origen: ESTADO_CAMA

* Comportamiento: Selección múltiple

* Alcance (Scoping): Todo el tablero

**Buscar Documento**

* Tipo: Value

* Columna Origen: NUMERO_DOCUMENTO

* Comportamiento: Búsqueda dinámica global

* Alcance (Scoping): Todo el tablero

## 9. Configuración CSS (Estilo y Alineación de KPIs)
Regla aplicada en Edit Dashboard > Edit CSS para forzar el centrado geométrico del valor numérico y su subtítulo:

```CSS

/* Centrar valor principal y subtítulo en todos los Big Numbers */
.big-number-chart, 
.IntelliHealth-legacy-chart-big-number,
[data-test="chart-container"] .header-line,
[data-test="chart-container"] .subheader-line {
    text-align: center !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
}
```