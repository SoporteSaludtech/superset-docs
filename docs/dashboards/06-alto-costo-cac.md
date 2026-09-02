# Consola y Cohortes CAC (Alto Costo)

Este módulo documenta la implementación de la consola analítica para el seguimiento de pacientes con patologías de alto costo (Cáncer, VIH, Renal y Huérfanas) integrado mediante Apache Superset y alimentado desde el motor transaccional de Hosvital HIS.

---

## 1. Arquitectura de Datos (SQL Server)
La capa de datos se sustenta en una vista optimizada en la base de datos HVT_REDHUMANA bajo el esquema dbo, la cual realiza un agrupamiento y desduplicación por paciente único (HISCKEY) por cada servicio hospitalario (mpnomp), incorporando el cálculo seguro en punto flotante para los porcentajes de cohorte.

```sql
USE [HVT_REDHUMANA];
GO

CREATE OR ALTER VIEW [dbo].[VW_Hosvital_CAC] AS
WITH Base_Pacientes AS (
    SELECT 
        MP.mpnomp,
        H.HISCKEY,
        MAX(CAST(D.Es_Cancer AS INT)) AS Es_Cancer,
        MAX(CAST(D.Es_VIH AS INT)) AS Es_VIH,
        MAX(CAST(D.Es_Renal AS INT)) AS Es_Renal,
        MAX(CAST(D.Es_Huerfana AS INT)) AS Es_Huerfana,
        MAX(H.HISCFCON) AS HISCFCON
    FROM [dbo].[HCDIAGN] AS HD WITH (NOLOCK)
    INNER JOIN [dbo].[Diagnosticos] AS D WITH (NOLOCK) ON HD.HCDXCOD = D.DMCodi
    INNER JOIN [dbo].[HCCOM1] AS H WITH (NOLOCK) ON HD.hisckey = H.HISCKEY AND HD.HISCSEC = H.HISCSEC
    INNER JOIN [dbo].[INGRESOS] AS I WITH (NOLOCK) ON H.HISCKEY = I.MPCedu AND H.HCtvIn1 = I.IngCsc
    LEFT JOIN [dbo].[MAEPAB] MP WITH (NOLOCK) ON I.mpcodp = MP.mpcodp
    WHERE (D.Es_Cancer = 1 OR D.Es_VIH = 1 OR D.Es_Renal = 1 OR D.Es_Huerfana = 1)
      AND I.mpcodp IS NOT NULL 
      AND I.mpcodp <> ''
    GROUP BY MP.mpnomp, H.HISCKEY
)
SELECT 
    ISNULL(mpnomp, '--- TOTAL INSTITUCIONAL ---') AS Servicio,
    COUNT(DISTINCT HISCKEY) AS Total_CAC,
    SUM(Es_Cancer) AS Casos_Cancer,
    SUM(Es_VIH) AS Casos_VIH,
    SUM(Es_Renal) AS Casos_Renal,
    SUM(Es_Huerfana) AS Casos_Huerfanas,
    CAST((SUM(CAST(Es_Cancer AS FLOAT)) * 100.0) / NULLIF(COUNT(DISTINCT HISCKEY), 0) AS DECIMAL(10,2)) AS Porc_Cancer,
    CAST((SUM(CAST(Es_VIH AS FLOAT)) * 100.0) / NULLIF(COUNT(DISTINCT HISCKEY), 0) AS DECIMAL(10,2)) AS Porc_VIH,
    CAST((SUM(CAST(Es_Renal AS FLOAT)) * 100.0) / NULLIF(COUNT(DISTINCT HISCKEY), 0) AS DECIMAL(10,2)) AS Porc_Renal,
    CAST((SUM(CAST(Es_Huerfana AS FLOAT)) * 100.0) / NULLIF(COUNT(DISTINCT HISCKEY), 0) AS DECIMAL(10,2)) AS Porc_Huerfanas,
    MAX(HISCFCON) AS FECHA_ATENCION
FROM Base_Pacientes
GROUP BY mpnomp;
GO;
```
## 2. Registro y Configuración en Apache Superset
Dataset: Registrar la vista bajo el nombre DS_Hosvital_CAC seleccionando el esquema dbo.

Columna Temporal: Marcar la columna FECHA_ATENCION como Is temporal para habilitar los filtros globales de tiempo en el dashboard.

Métricas y Agregaciones: Configurar las métricas numéricas y porcentuales utilizando agregaciones de tipo MAX para evitar que Superset vuelva a sumar valores precalculados por la vista.

Ordenamiento Inicial: Configurar la propiedad Sort query by seleccionando la columna Servicio en modo Ascendente (A-Z).

## 3. Reglas de Semaforización (Formato Condicional)
Para estandarizar la lectura visual del riesgo por servicio, las celdas numéricas se configuran con las siguientes reglas de umbrales:

1. Verde (Valores Bajos / Seguros): Operador ≤ x ≤ para el intervalo entre 0 y 15.

2. Amarillo (Valores Intermedios): Operador < x ≤ para el intervalo entre 15 y 40.

3. Rojo (Valores Críticos / Altos): Operador > para valores mayores a 30 / 40.
