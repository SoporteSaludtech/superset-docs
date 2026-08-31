# Gestión de Calidad: Vigilancia Epidemiológica e IAAS

*   **Módulo de Origen:** Historia Clínica / Diagnósticos (`HCDIAGN`, `MAEDIA`, `HCCOM1`, `Ingresos`, `Capbas`).[cite: 2]
*   **Propósito:** Detección, aislamiento y seguimiento de infecciones asociadas a la atención en salud (IAAS) y patologías de interés en salud pública.[cite: 2]
*   **Frecuencia de Actualización:** 15 minutos.[cite: 2]

---

## 1. Alcance Conceptual y Fórmulas Matemáticas

### Índice de Presión Infecciosa por 100 Camas-Día
Mide la prevalencia de infecciones activas normalizada por los días de estancia acumulados:[cite: 2]

$$\text{Índice IAAS} = \left( \frac{\text{Total Pacientes con Infección Activa}}{\sum \text{Días de Estancia Acumulados}} \right) \times 100$$

### Criterios de Interpretación Epidemiológica
*   **Índice <= 3.0% (Controlado):** Comportamiento esperado dentro de los límites de control.[cite: 2]
*   **Índice > 3.0% (Alerta Temprana de Brote):** Requiere activación de rondas de bioseguridad, tipificación microbiológica y desinfección terminal.[cite: 2]

---

## 2. Especificación Técnica T-SQL

```sql
SELECT 
    i.IngCsc AS CONSECUTIVO_INGRESO,
    i.MPCedu AS NUMERO_IDENTIFICACION,
    i.MPTDoc AS TIPO_IDENTIFICACION,
    c.MPNomC AS NOMBRE_PACIENTE,
    c.MPSexo AS SEXO,
    DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON) - 
    CASE 
        WHEN (MONTH(c.MPFchN) > MONTH(c1.HISCFCON)) OR 
             (MONTH(c.MPFchN) = MONTH(c1.HISCFCON) AND DAY(c.MPFchN) > DAY(c1.HISCFCON)) 
        THEN 1 ELSE 0 
    END AS EDAD,
    CASE 
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 0 AND 4   THEN '00-04 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 5 AND 9   THEN '05-09 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 10 AND 14 THEN '10-14 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 15 AND 19 THEN '15-19 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 20 AND 24 THEN '20-24 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 25 AND 29 THEN '25-29 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 30 AND 34 THEN '30-34 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 35 AND 39 THEN '35-39 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 40 AND 44 THEN '40-44 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 45 AND 49 THEN '45-49 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 50 AND 54 THEN '50-54 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 55 AND 59 THEN '55-59 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 60 AND 64 THEN '60-64 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 65 AND 69 THEN '65-69 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 70 AND 74 THEN '70-74 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) BETWEEN 75 AND 79 THEN '75-79 Años'
        WHEN (DATEDIFF(YEAR, c.MPFchN, c1.HISCFCON)) >= 80              THEN '80+ Años'
        ELSE 'Sin Edad Registrada'
    END AS GRUPO_QUINQUENAL,
    c1.HISCFCON AS FECHA_DIAGNOSTICO,
    i.IngFecAdm AS FECHA_INGRESO,
    i.IngFecEgr AS FECHA_EGRESO,
    pab.MPNomP AS SERVICIO_ACTUAL,
    CASE i.ClaPro
        WHEN 1 THEN 'Ambulatorio'
        WHEN 2 THEN 'Hospitalización'
        WHEN 3 THEN 'Urgencias'
        ELSE 'Otro'
    END AS TIPO_ATENCION,
    LTRIM(RTRIM(hc.HCDXCOD)) AS CODIGO_CIE10,
    d.DMNomb AS DIAGNOSTICO,
    'Infecciosas / IAAS' AS CATEGORIA_EPIDEMIOLOGICA,
    emp.MENOMB AS CONTRATO_EMPRESA,
    CASE 
        WHEN i.IngFecEgr IS NULL OR i.IngFecEgr <= '1753-01-01' OR i.IngFecEgr = ''
        THEN CASE 
                WHEN i.IngFecAdm IS NOT NULL AND i.IngFecAdm > '1753-01-01'
                THEN DATEDIFF(DAY, i.IngFecAdm, GETDATE()) + 1
                ELSE 1 
             END
        WHEN i.IngFecAdm IS NULL OR i.IngFecAdm <= '1753-01-01' THEN 1
        ELSE CASE 
                WHEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) >= 0 
                THEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) + 1 
                ELSE 1 
             END
    END AS DIAS_ESTANCIA_ACUMULADOS
FROM dbo.HCDIAGN hc
INNER JOIN dbo.MAEDIA d ON LTRIM(RTRIM(hc.HCDXCOD)) = LTRIM(RTRIM(d.DMCodi))
INNER JOIN dbo.HCCOM1 c1 ON hc.hisckey = c1.HISCKEY AND hc.HISCSEC = c1.HISCSEC
INNER JOIN dbo.Ingresos i ON hc.hisckey = i.MPCedu AND c1.HISTIPDOC = i.MPTDoc
INNER JOIN dbo.Capbas c ON i.MPCedu = c.MPCedu AND i.MPTDoc = c.MPTDoc
LEFT JOIN dbo.Maepab pab ON i.MPCodP = pab.MPCodP
LEFT JOIN dbo.Maeemp emp ON i.IngNit = emp.MENNIT
WHERE (hc.HCDXCOD LIKE 'A%' OR hc.HCDXCOD LIKE 'B%' OR hc.HCDXCOD LIKE 'J0%' OR hc.HCDXCOD LIKE 'J1%' OR hc.HCDXCOD LIKE 'N


## 3. Diccionario de Componentes Visuales

|Componente|  Tipo de Visualización | Métrica / Dimensión| Objetivo Operativo |
| :--- | :--- | :--- | :--- |



|**Índice IAAS**|  Big Number| (COUNT(DISTINCT ID)*100.0) / NULLIF(SUM(ESTANCIA), 0)| Presión infecciosa sobre camas ocupadas.|
|**Matriz Térmica**| (Heatmap)Mapa de Calor Diagnóstico| CIE-10 vs Grupo Etario| Identificación de poblaciones vulnerables.|
|**Aislamientos por Pabellón**| Gráfico Circular (Donut)| SERVICIO_ACTUAL | Distribución de carga asistencial de bioseguridad.|
|**Consola Epidemiológica Tabla Interactiva Paciente**| CIE-10| Estancia| Pabellón Herramienta de ronda para el Comité de Infecciones.|

4. Parámetros Operativos y Filtros (Superset)
1. El tablero cuenta con reglas de formato condicional (Color Formatting) y filtros maestros diseñados para la gestión ágil del Comité de Infecciones:
2. Alerta de Población Vulnerable (Warning): Resalta en color ámbar las celdas de pacientes pediátricos (menores de 5 años) y geriátricos (mayores o iguales a 65 años) mediante reglas de validación múltiple (< 5 y >= 65).
3. Control de Estancia (Cell Bars): La columna DIAS_ESTANCIA_ACUMULADOS proyecta una barra de calor interna y se ordena de manera descendente para enfocar la auditoría en los pacientes con mayor riesgo de complicaciones.
4. Filtro Maestro Temporal: Configurado unificadamente sobre la columna FECHA_DIAGNOSTICO en todos los gráficos, permitiendo auditar cohortes infecciosas recientes (ej. "Últimos 7 días") sin verse distorsionado por fechas de ingreso antiguas.
5. Filtros Cruzados: Selectores dinámicos integrados para cruzar variables por Pabellón, Código CIE-10, Tipo de Atención y EPS.