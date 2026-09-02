# 08 - Consola de Gestión y Cohortes: Enfermedades Crónicas

## 1. Marco Conceptual y Fundamento Clínico-Epidemiológico

### 1.1. Propósito y Alcance Asistencial
Las Enfermedades Crónicas No Transmisibles (ECNT) constituyen la mayor carga de morbilidad, años de vida ajustados por discapacidad (AVAD) y costos asistenciales evitables dentro del sistema de salud. La **Consola de Gestión y Cohortes - Enfermedades Crónicas** es una solución de analítica avanzada y monitorización en tiempo de ejecución construida sobre **Apache Superset** y **Microsoft SQL Server (Hosvital HIS)**.

El objetivo central del tablero es operacionalizar la **Gestión del Riesgo en Salud (GDR)** mediante cuatro pilares:

1. **Identificación nominal de cohortes:** Agrupación dinámica de pacientes en programas de Hipertensión Arterial (HTA), Diabetes Mellitus Tipo 2 (DM2) y Enfermedad Pulmonar Obstructiva Crónica (EPOC).
2. **Control clínico objetivo:** Monitorización de metas terapéuticas basadas en evidencia científica (presión arterial estandarizada y hemoglobina glicosilada).
3. **Mitigación de eventos adversos y reingresos:** Alerta y detección de atenciones hospitalarias posteriores en pacientes vulnerables para reducir estancias no planificadas.
4. **Gobernanza demográfica y de aseguramiento:** Segmentación por quinquenios de edad, sexo biológico y entidades contratantes (EPS / Convenios) para equilibrar la oferta de servicios ambulatorios vs. hospitalarios.

### 1.2. Definición de Cohortes y Criterios Clínicos

| Patología | Clasificación CIE-10 | Criterio de Control / Evento Monitoreado |
| :--- | :--- | :--- |
| **Hipertensión Arterial (HTA)** | I10X (Primaria/Esencial) | Presión Sistólica **< 140 mmHg** y Diastólica **< 90 mmHg** (Guías ACC/AHA / ESH). |
| **Diabetes Mellitus Tipo 2 (DM2)** | E110 - E119 (DM2 no insulinodependiente) | Hemoglobina Glicosilada (HbA1c) **<= 7.0%** (Estándares ADA). |
| **Enfermedad Pulmonar Obstructiva Crónica (EPOC)** | J440 - J449 (Otras EPOC / Exacerbaciones) | Ausencia de Reingreso Hospitalario Posterior (Guías GOLD). |

---

## 2. Arquitectura de Datos y Modelado SQL Server

### 2.1. Modelo Relacional Subyacente (Hosvital HIS)
El modelo se alimenta de transacciones asistenciales registradas en tiempo real en la base de datos `HVT_REDHUMANA`:

* **`CAPBAS` (Maestro de Pacientes):** Identificación (`MPCedu`), nombre completo (`MPNomC`), teléfono (`MPTele`), fecha de nacimiento y sexo.
* **`HCCOM1` (Encabezado de Consulta Externa / Urgencias):** Llave de atención (`HISCKEY`), consecutivo (`HISCSEC`), fecha y hora de la consulta (`HISCFCON`), contrato (`FHCCodCto`).
* **`HCDIAGN` y `Diagnosticos`:** Registro de diagnósticos por consulta (`HCDXCOD`), tipo de diagnóstico (`HCDXTIP`: `CN`, `CR`) y catálogo CIE-10 (`DMCodi`).
* **`SGNVTLH` (Signos Vitales):** Presión arterial sistólica (`HISDPRES`), diastólica (`HISDPRED`) y hora de toma.
* **`HCCOM51` (Resultados de Laboratorios):** Código CUPS (`HCPrcCod`), resultado alfanumérico (`HCRESULT`). Códigos HbA1c: `903426` y `903427`.
* **`INGRESOS` (Admisiones Institucionales):** Consecutivo de ingreso (`IngCsc`) para el cálculo de reingreso posterior.
* **`MAEEMP` (Maestro de Empresas):** Razón social de la entidad pagadora (`MENOMB`).

> **Nota Técnica:** Todas las vistas exponen la columna temporal unificada `FECHA_ATENCION` tipificada como `DATETIME` nativo, configurada en Superset con la bandera `Is temporal = True` para habilitar los filtros globales.

### 2.2. Definiciones DDL de las Vistas del Modelo

**Vista 1: VW_Cronicos_KPI_HTA**
```sql
CREATE OR ALTER VIEW [dbo].[VW_Cronicos_KPI_HTA] AS
SELECT 
    H.HISCKEY,
    CAST(H.HISCFCON AS DATETIME) AS FECHA_ATENCION,
    SV.HISDPRES AS Presion_Sistolica,
    SV.HISDPRED AS Presion_Diastolica,
    CASE 
        WHEN SV.HISDPRES > 0 AND SV.HISDPRED > 0 
         AND SV.HISDPRES < 140 AND SV.HISDPRED < 90 THEN 1 
        ELSE 0 
    END AS Cumple_Meta
FROM [dbo].[HCCOM1] AS H WITH (NOLOCK)
INNER JOIN [dbo].[HCDIAGN] AS HD WITH (NOLOCK) 
    ON H.HISCKEY = HD.hisckey AND H.HISCSEC = HD.HISCSEC
INNER JOIN [dbo].[Diagnosticos] AS D 
    ON LTRIM(RTRIM(HD.HCDXCOD)) = LTRIM(RTRIM(D.DMCodi))
INNER JOIN [dbo].[SGNVTLH] AS SV WITH (NOLOCK) 
    ON H.HISCKEY = SV.HISCKEY AND H.HISCSEC = SV.HISCSEC
WHERE D.DMCodi LIKE 'I10%' 
  AND HD.HCDXTIP IN ('CN', 'CR')
  AND SV.HISDPRES > 0;
```  
Vista 2: VW_Cronicos_KPI_DM2

```SQL
CREATE OR ALTER VIEW [dbo].[VW_Cronicos_KPI_DM2] AS
SELECT 
    H.HISCKEY,
    CAST(H.HISCFCON AS DATETIME) AS FECHA_ATENCION,
    LAB.HCRESULT AS Resultado_HbA1c,
    CASE 
        WHEN TRY_CONVERT(DECIMAL(6, 2), REPLACE(LTRIM(RTRIM(LAB.HCRESULT)), ',', '.')) <= 7.00 THEN 1
        ELSE 0 
    END AS Cumple_Meta
FROM [dbo].[HCCOM1] AS H WITH (NOLOCK)
INNER JOIN [dbo].[HCDIAGN] AS HD WITH (NOLOCK) 
    ON H.HISCKEY = HD.hisckey AND H.HISCSEC = HD.HISCSEC
INNER JOIN [dbo].[Diagnosticos] AS D 
    ON LTRIM(RTRIM(HD.HCDXCOD)) = LTRIM(RTRIM(D.DMCodi))
LEFT JOIN [dbo].[HCCOM51] AS LAB WITH (NOLOCK) 
    ON H.HISCKEY = LAB.HISCKEY 
    AND H.HISCSEC = LAB.HISCSEC 
    AND LAB.HCPrcCod IN ('903426', '903427')
WHERE D.DMCodi LIKE 'E11%' 
  AND HD.HCDXTIP IN ('CN', 'CR');
```
Vista 3: VW_Cronicos_KPI_EPOC

```SQL
CREATE OR ALTER VIEW [dbo].[VW_Cronicos_KPI_EPOC] AS
SELECT 
    H.HISCKEY,
    CAST(H.HISCFCON AS DATETIME) AS FECHA_ATENCION,
    CASE 
        WHEN EXISTS (
            SELECT 1 
            FROM [dbo].[INGRESOS] AS I WITH (NOLOCK) 
            WHERE I.MPCedu = H.HISCKEY 
              AND I.IngCsc > H.HCtvIn1
        ) THEN 1 
        ELSE 0 
    END AS Tuvo_Reingreso
FROM [dbo].[HCCOM1] AS H WITH (NOLOCK)
INNER JOIN [dbo].[HCDIAGN] AS HD WITH (NOLOCK) 
    ON H.HISCKEY = HD.hisckey AND H.HISCSEC = HD.HISCSEC
INNER JOIN [dbo].[Diagnosticos] AS D 
    ON LTRIM(RTRIM(HD.HCDXCOD)) = LTRIM(RTRIM(D.DMCodi))
WHERE D.DMCodi LIKE 'J44%' 
  AND HD.HCDXTIP IN ('CN', 'CR');
```  
## 3. Ficha Metodológica de Indicadores y Fórmulas Aritméticas

### 3.1. Porcentaje de Control Tensional en HTA
* **Criterio Clínico:** Pacientes con Presión Sistólica < 140 mmHg y Diastólica < 90 mmHg.
* **Fórmula Aritmética:**

> $$\% \text{ Control HTA} = \left( \frac{\text{Atenciones con PAS } < 140 \text{ y PAD } < 90}{\text{Total Atenciones Evaluadas de HTA}} \right) \times 100$$

* **Expresión Custom SQL:**
```sql
COALESCE(SUM(Cumple_Meta) * 1.0 / NULLIF(COUNT(*), 0), 0);
```
Formato: Porcentaje con 2 decimales (%,.2f).

### 3.2. Porcentaje de Control Metabólico en DM2
* **Criterio: Reporte numérico de HbA1c <= 7.0%.**

* **Fórmula Aritmetica:**

$$\% \text{ Control DM2} = \left( \frac{\text{Atenciones DM2 con HbA1c } \le 7.0\%}{\text{Total Atenciones Evaluadas de DM2}} \right) \times 100$$

* **Expresión Custom SQL:**

```SQL
COALESCE(SUM(Cumple_Meta) * 1.0 / NULLIF(COUNT(*), 0), 0):
```
Formato: Porcentaje con 2 decimales (%,.2f).

### 3.3. Tasa de Reingreso Hospitalario en EPOC
* **Criterio:** Paciente con diagnóstico de EPOC con readmisión hospitalaria institucional posterior.

* **Fórmula Aritmetica:**
$$ \text{Tasa Reingreso EPOC} = \left( \frac{\sum_{k=1}^{p} \text{Tuvo_Reingreso}k}{P{EPOC}} \right) \times 100 $$

* **Expresión Custom SQL:**

```SQL
COALESCE(SUM(Tuvo_Reingreso) * 1.0 / NULLIF(COUNT(*), 0), 0)
```
Formato: Porcentaje con 2 decimales (%,.2f).

## 4. Estructura Visual y Filtros Nativos

### 4.1. Catálogo de Visualizaciones
Panel / Visualización	Tipo de Gráfico en Superset	Configuración Destacada
KPIs Ejecutivos	Big Number with Trendline	Grano temporal mensual. Gradiente activado. Ancho: 4 columnas cada uno.
Estructura Demográfica	ECharts Bar Chart	Barras apiladas (Stacked). Eje X: Grupo Etario. Desglose: Sexo.
Consola Nominal	Table (Raw Records)	Buscador de texto habilitado. Paginación activa a 25 registros.

### 4.2. Filtros Nativos Globales
El tablero implementa un panel retráctil lateral con filtros sincronizados:

Periodo de Análisis: Temporal (Time range) anclado a la columna FECHA_ATENCION.

Cohorte Patológica: Selección múltiple (Value filter) sobre la columna Cohorte (HTA, DM2, EPOC).

Asegurador / EPS: Búsqueda dinámica (Value filter) sobre la columna Entidad_Contrato.

## 5. Interpretación Clínica y Protocolos de Acción
### 5.1. Matriz de Semaforización Operativa
Indicador	Óptimo (Verde)	Alerta (Amarillo)	Crítico (Rojo)
% Control Tensional (HTA)	>= 75.0%	60.0% - 74.9%	< 60.0%
% Control Metabólico (DM2)	>= 65.0%	50.0% - 64.9%	< 50.0%
Tasa Reingreso Hospitalario (EPOC)	< 5.0%	5.0% - 10.0%	> 10.0%

### 5.2. Protocolo de Gestión ante Desviaciones
Desviación en Control HTA (< 60%): Filtrar en la consola nominal por Cohorte = 'HTA' y Presion_Sistolica >= 140. Exportar el listado a CSV para agendamiento prioritario y ajuste terapéutico.

Desviación en Control DM2 (< 50%): Verificar en la tabla maestra si existe brecha de tamizaje (pacientes sin paraclínico tomado en los últimos 6 meses) y activar ruta de llamado institucional.

Incremento en Tasa de Reingreso EPOC (> 10%): Filtrar en la consola por Tiene_Ingreso_Posterior = 1 y realizar auditoría médica concurrente para identificar factores de falla terapéutica o necesidad de oxígeno domiciliario.