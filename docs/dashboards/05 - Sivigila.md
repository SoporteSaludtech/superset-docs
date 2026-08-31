# Módulo de Vigilancia en Salud Pública (SIVIGILA)

Este tablero consolida la información clínica y epidemiológica para la detección oportuna, seguimiento y notificación de eventos de interés en salud pública, permitiendo a la auditoría médica y al comité de epidemiología el control nominal de los casos obligatorios en la institución.

---

## 1. Definición del Dataset Base (DS_Hosvital_SIVIGILA)
Los datos se obtienen mediante un modelo relacional que cruza la información de atenciones clínicas (HCCOM1), diagnósticos registrados (HCDIAGN) y el maestro normativo de patologías de notificación obligatoria (Diagnosticos).

`sql
SELECT 
    C1.HISCKEY AS NUMERO_IDENTIFICACION,
    C1.HISCSEC AS CONSECUTIVO_ATENCION,
    C1.HISCFCON AS FECHA_ATENCION,
    C1.HISCMMED AS MEDICO_TRATANTE,
    ISNULL(LTRIM(RTRIM(HC.HCDXCOD)), 'Sin Registro') AS CODIGO_CIE10,
    ISNULL(D.DMNomb, 'Diagnóstico No Codificado') AS DIAGNOSTICO_NOMBRE, 
    ISNULL(CAST(D.Es_Sivigila AS INT), 0) AS FLAG_SIVIGILA,
    ISNULL(CAST(D.Es_ETV AS INT), 0) AS FLAG_ETV,
    ISNULL(CAST(D.Es_ETS AS INT), 0) AS FLAG_ETS,
    1 AS PACIENTE_ATENDIDO
FROM [dbo].[HCCOM1] AS C1
LEFT JOIN [dbo].[HCDIAGN] AS HC 
    ON C1.HISCKEY = HC.hisckey AND C1.HISCSEC = HC.HISCSEC
LEFT JOIN [dbo].[Diagnosticos] AS D 
    ON LTRIM(RTRIM(HC.HCDXCOD)) = LTRIM(RTRIM(D.DMCodi))
WHERE C1.HISCFCON > '1753-01-01';
```

. Componentes del Tablero (Charts)
El tablero se compone de 4 visualizaciones principales diseñadas para el monitoreo gerencial y operativo:

A. Indicadores Clave de Desempeño (KPIs)
Índice de Detección SIVIGILA (Big Number): Mide el porcentaje de pacientes atendidos que requieren notificación obligatoria.

Fórmula de Métrica: (SUM(FLAG_SIVIGILA) * 100.0) / NULLIF(COUNT(DISTINCT NUMERO_IDENTIFICACION), 0)

Formato: Porcentual con dos decimales (.2f%).

Total Casos SIVIGILA (Big Number): Volumen bruto de fichas sujetas a reporte ante el Instituto Nacional de Salud (INS).

Métrica: SUM(FLAG_SIVIGILA)

B. Análisis Epidemiológico
Transmisibilidad ETV vs ETS (Bar Chart / Custom): Compara de forma directa la carga de patologías transmitidas por vectores (Dengue, Malaria) frente a las de transmisión sexual para priorización de campañas de prevención.

Métricas: SUM(FLAG_ETV) vs SUM(FLAG_ETS).

C. Consola Operativa y de Auditoría
Consola Nominal SIVIGILA (Table): Listado detallado y filtrado exclusivamente para revisión médica de omisiones de fichas o errores de codificación.

Modo: Raw records.

Columnas: Fecha de Atención, Consecutivo, Identificación, Código CIE-10, Nombre del Diagnóstico y Médico Tratante.

Filtro Fijo: FLAG_SIVIGILA = 1.

3. Interactividad y Filtros
Filtro Nativo de Tiempo: El tablero cuenta con un filtro maestro de tipo Time range vinculado a la columna FECHA_ATENCION del dataset, permitiendo segmentar el análisis por rangos personalizados (diario, semanal, mensual o anual) de forma simultánea en todas las vistas.
