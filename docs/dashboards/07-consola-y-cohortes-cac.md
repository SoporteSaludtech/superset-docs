# Ficha Técnica: Dashboard 07 - Consola y Cohortes CAC (Demografía)

Este documento detalla la especificación técnica, la arquitectura de base de datos y la configuración de visualización en Apache Superset para el cuadro de mando de **Consola y Cohortes CAC**, enfocado en el análisis demográfico, estratificación por quinquenios y distribución por sexo de pacientes con patologías de alto costo (Cáncer, VIH, Renal y Huérfanas).

---

## 1. Arquitectura de Datos (SQL Server)

La capa analítica se alimenta de la vista desipivotada VW_Hosvital_CAC_Demografia, la cual procesa el universo de pacientes únicos, calcula las edades a partir de la fecha de atención y categoriza los rangos quinquenales.

```sql
USE [HVT_REDHUMANA];
GO

CREATE OR ALTER VIEW [dbo].[VW_Hosvital_CAC_Demografia] AS
WITH Pacientes_CAC AS (
    SELECT 
        I.mpcodp,
        P.MPCedu,
        P.MPSexo,
        P.MPFchN,
        MAX(H.HISCFCON) AS FECHA_ATENCION,
        MAX(CAST(D.Es_Cancer AS INT)) AS Es_Cancer,
        MAX(CAST(D.Es_VIH AS INT)) AS Es_VIH,
        MAX(CAST(D.Es_Renal AS INT)) AS Es_Renal,
        MAX(CAST(D.Es_Huerfana AS INT)) AS Es_Huerfana
    FROM [dbo].[HCDIAGN] AS HD WITH (NOLOCK)
    INNER JOIN [dbo].[Diagnosticos] AS D WITH (NOLOCK) ON HD.HCDXCOD = D.DMCodi
    INNER JOIN [dbo].[HCCOM1] AS H WITH (NOLOCK) ON HD.hisckey = H.HISCKEY AND HD.HISCSEC = H.HISCSEC
    INNER JOIN [dbo].[INGRESOS] AS I WITH (NOLOCK) ON H.HISCKEY = I.MPCedu AND H.HCtvIn1 = I.IngCsc
    INNER JOIN [dbo].[CAPBAS] AS P WITH (NOLOCK) ON H.HISCKEY = P.MPCedu
    WHERE (D.Es_Cancer = 1 OR D.Es_VIH = 1 OR D.Es_Renal = 1 OR D.Es_Huerfana = 1)
      AND I.mpcodp IS NOT NULL 
      AND I.mpcodp <> ''
    GROUP BY I.mpcodp, P.MPCedu, P.MPSexo, P.MPFchN
),
Categorizacion AS (
    SELECT 
        *,
        (CONVERT(int,CONVERT(char(8),FECHA_ATENCION,112))-CONVERT(int,CONVERT(char(8),MPFchN,112)))/10000 AS Edad
    FROM Pacientes_CAC
),
Grupos_Quinquenales AS (
    SELECT 
        *,
        CASE 
            WHEN Edad BETWEEN 0 AND 4 THEN '00-04' WHEN Edad BETWEEN 5 AND 9 THEN '05-09'
            WHEN Edad BETWEEN 10 AND 14 THEN '10-14' WHEN Edad BETWEEN 15 AND 19 THEN '15-19'
            WHEN Edad BETWEEN 20 AND 24 THEN '20-24' WHEN Edad BETWEEN 25 AND 29 THEN '25-29'
            WHEN Edad BETWEEN 30 AND 34 THEN '30-34' WHEN Edad BETWEEN 35 AND 39 THEN '35-39'
            WHEN Edad BETWEEN 40 AND 44 THEN '40-44' WHEN Edad BETWEEN 45 AND 49 THEN '45-49'
            WHEN Edad BETWEEN 50 AND 54 THEN '50-54' WHEN Edad BETWEEN 55 AND 59 THEN '55-59'
            WHEN Edad BETWEEN 60 AND 64 THEN '60-64' WHEN Edad BETWEEN 65 AND 69 THEN '65-69'
            WHEN Edad BETWEEN 70 AND 74 THEN '70-74' WHEN Edad BETWEEN 75 AND 79 THEN '75-79'
            ELSE '80+' 
        END AS Grupo_Quinquenal
    FROM Categorizacion
)
SELECT 
    ISNULL(MP.mpnomp, 'PABELLÓN NO DEFINIDO') AS Pabellon,
    G.MPSexo AS Sexo,
    G.Grupo_Quinquenal,
    G.FECHA_ATENCION,
    G.MPCedu AS Id_Paciente,
    Cohorte.Nombre_Cohorte AS Cohorte
FROM Grupos_Quinquenales G
LEFT JOIN [dbo].[MAEPAB] MP WITH (NOLOCK) ON G.mpcodp = MP.mpcodp
CROSS APPLY (
    VALUES 
        ('Cáncer', Es_Cancer),
        ('VIH', Es_VIH),
        ('Renal', Es_Renal),
        ('Huérfanas', Es_Huerfana)
) AS Cohorte(Nombre_Cohorte, Tiene_Cohorte)
WHERE Cohorte.Tiene_Cohorte = 1;
GO;
```
## 2. Registro del Dataset en Apache Superset
Nombre del Dataset: DS_Hosvital_CAC_Demografia

Columna Temporal: Marcar FECHA_ATENCION como Is temporal para habilitar el filtrado cronológico.

Métrica Principal Configurada:

Nombre: Pacientes CAC Únicos

Expresión SQL / Agregación: COUNT_DISTINCT(Id_Paciente)

Propósito: Garantiza que si un paciente tiene múltiples atenciones en el mes para la misma cohorte, el sistema lo contabilice de manera unívoca.

## 3. Configuración de Visualizaciones y Personalización (Customize)
A. Gráfico de Distribución por Cohorte y Sexo (Pie / Donut / Sunburst)
Dimensiones (Dimensions): Cohorte, seguida de Sexo (MPSexo).

Estilo Dona (Donut Chart): Configurar el radio interior (Inner Radius) entre 40 y 60 para optimizar la estética ejecutiva.

Etiquetas (Label Type): Configurado como Key, value and percent para mostrar simultáneamente la cohorte, el conteo absoluto de pacientes únicos y la proporción porcentual.

Leyenda: Ubicada en el panel derecho (Right) con desplazamiento activado (Scrollable) para manejar dinámicamente cohortes con menor volumen.

## 4. Filtros Nativos Transversales del Dashboard
El tablero integra controles superiores sincronizados que afectan de manera simultánea los componentes institucionales y demográficos:

1. Filtro de Fecha (Mes): Conectado a la columna temporal de los datasets.

2. Filtro de Servicio / Pabellón: Sincronizado con Servicio y Pabellon.

3. Filtro de Grupo Quinquenal: Permite acotar el análisis por rangos etarios quinquenales.

4. Filtro de Sexo: Filtra dinámicamente la población de estudio según MPSexo.
