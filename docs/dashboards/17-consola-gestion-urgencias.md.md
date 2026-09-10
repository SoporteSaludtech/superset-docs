# Documentación: Consola de Gestión de Urgencias

## 1. Ficha Técnica General
* **Nombre del Tablero:** Consola de Gestión de Urgencias
* **Plataforma Analítica:** IntelliHealth 6.1.0 (Apache Superset)
* **Sistema Origen:** Hosvital HIS (Microsoft SQL Server)
* **Módulo de Referencia:** Admisiones, Urgencias, Historia Clínica
* **Frecuencia de Actualización:** Tiempo Real (Direct Query a la vista)
* **Nivel de Acceso:** Coordinación Médica, Jefatura de Urgencias, Auditoría Concurrente.

---

## 2. Propósito y Alcance

### 2.1 Propósito
Proveer un tablero de control operativo y gerencial que permita monitorear en tiempo real el flujo de pacientes, la ocupación física, la distribución de la carga asistencial por especialidad y la composición de los pagadores dentro del servicio de Urgencias. Facilita la toma de decisiones ágiles para evitar la saturación de los recursos físicos y humanos.

### 2.2 Alcance
El tablero consolida los episodios asistenciales tipificados bajo la modalidad de atención de Urgencias y Triage. Contempla desde el registro administrativo (admisión) hasta el egreso hospitalario, priorizando el monitoreo de los pacientes "Activos" y habilitando el análisis retrospectivo mediante el cálculo de estancias para los episodios ya cerrados.

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en HOSVITAL HIS
* **`INGRESOS`**: Encabezado principal del episodio asistencial (Fechas, Pagador, Pabellón físico, Tipificación ClaPro, Especialidad tratante `IngEsMt`).
* **`CAPBAS`**: Información demográfica del paciente (Documento, Nombre, Sexo, Fecha de Nacimiento).
* **`MAEPAB`**: Maestro de Pabellones y Áreas Físicas.
* **`MAEESP`**: Maestro de Especialidades Médicas (`MAEESP.mecode`).
* **`MAEEMP`**: Maestro de Empresas / Aseguradoras.
* **`HCDIAGN`**: Detalle de diagnósticos registrados en la Historia Clínica, utilizado para extraer el diagnóstico principal del episodio.
* **`MAEDIA`**: Catálogo CIE-10 para la descripción clínica del diagnóstico.

### 3.2 DDL de la Vista Semántica Actualizada
La siguiente vista materializa el modelo estrella plano para el consumo directo desde IntelliHealth 6.1.0:

```sql
CREATE OR ALTER VIEW dbo.vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
AS
/***************************************************************************************************
* Vista: dbo.vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
* Objetivo: Fuente de datos para Consola de Gestión Asistencial en Urgencias
* Motor: Microsoft SQL Server (Hosvital HIS)
***************************************************************************************************/
SELECT 
    I.IngCsc                                                    AS CONSECUTIVO_INGRESO,
    I.mpcedu                                                    AS NUMERO_IDENTIFICACION,
    I.mptdoc                                                    AS TIPO_IDENTIFICACION,
    C.mpnomc                                                    AS PACIENTE,
    C.mpsexo                                                    AS GENERO,
    DATEDIFF(YEAR, C.mpfchn, I.ingfecadm)                       AS EDAD_INGRESO,
    I.ingfecadm                                                 AS FECHA_INGRESO,
    CAST(I.ingfecadm AS DATE)                                   AS FECHA_INGRESO_CORTE,
    DATEPART(YEAR, I.ingfecadm)                                 AS ANIO_INGRESO,
    DATEPART(MONTH, I.ingfecadm)                                AS MES_INGRESO,
    DATEPART(HOUR, I.ingfecadm)                                 AS HORA_INGRESO,
    CASE WHEN I.ingfecegr > '1753-01-01' THEN I.ingfecegr ELSE NULL END AS FECHA_EGRESO,
    CASE WHEN I.ingfecegr > '1753-01-01' THEN CAST(I.ingfecegr AS DATE) ELSE NULL END AS FECHA_EGRESO_CORTE,
    CASE WHEN I.ingfecegr > '1753-01-01' THEN 'EGRESADO' ELSE 'ACTIVO / EN OBSERVACION' END AS ESTADO_ATENCION,
    CASE 
        WHEN I.ingfecegr > '1753-01-01' THEN 
            CASE 
                WHEN DATEDIFF(DAY, I.ingfecadm, I.ingfecegr) >= 0 THEN DATEDIFF(DAY, I.ingfecadm, I.ingfecegr) + 1
                ELSE 1 
            END
        ELSE NULL 
    END                                                         AS DIAS_ESTANCIA,
    I.clapro                                                    AS CODIGO_CLAPRO,
    CASE CAST(I.clapro AS VARCHAR(5))
        WHEN '1' THEN 'Ambulatorio'
        WHEN '2' THEN 'Hospitalizacion'
        WHEN '3' THEN 'Urgencias'
        WHEN '4' THEN 'Tratamiento Especial'
        WHEN '5' THEN 'Triage'
        ELSE 'Otro / No Especificado'
    END                                                         AS TIPO_ATENCION,
    I.mpcodp                                                    AS CODIGO_PABELLON,
    ISNULL(NULLIF(LTRIM(RTRIM(M.mpnomp)), ''), 'Consulta Externa') AS SERVICIO_INGRESO,
    ISNULL(NULLIF(LTRIM(RTRIM(I.mpnumc)), ''), 'Sin Cama')      AS CAMA_ASIGNADA,
    I.ingnit                                                    AS NIT_ASEGURADORA,
    ISNULL(E.menomb, 'Particular / Sin Empresa')                AS ASEGURADORA,
    I.IngEsMt                                                   AS CODIGO_ESPECIALIDAD,
    ISNULL(ESP.menome, 'Especialidad No Registrada')            AS ESPECIALIDAD_TRATANTE,
    COALESCE(
        NULLIF(LTRIM(RTRIM(DX.HCDXCOD)), ''),
        NULLIF(LTRIM(RTRIM(I.ingentdx)), ''),
        'SIN_DX'
    )                                                           AS CODIGO_CIE10,
    ISNULL(D.DMNOMB, 'Sin Diagnóstico Registrado')              AS DIAGNOSTICO_PRINCIPAL

FROM dbo.INGRESOS I WITH (NOLOCK)
INNER JOIN dbo.CAPBAS C WITH (NOLOCK) 
    ON I.mpcedu = C.mpcedu AND I.mptdoc = C.mptdoc
LEFT JOIN dbo.MAEPAB M WITH (NOLOCK) 
    ON I.mpcodp = M.mpcodp
LEFT JOIN dbo.MAEEMP E WITH (NOLOCK) 
    ON I.ingnit = E.mennit
LEFT JOIN dbo.MAEESP ESP WITH (NOLOCK)
    ON I.IngEsMt = ESP.mecode
LEFT JOIN (
    SELECT 
        HISTipDoc, LTRIM(RTRIM(HISCKEY)) AS HISCKEY, HISCSEC, HCDXCOD,
        ROW_NUMBER() OVER (
            PARTITION BY HISTipDoc, LTRIM(RTRIM(HISCKEY)), HISCSEC 
            ORDER BY CASE WHEN HCDXCLS = 1 THEN 0 ELSE 1 END, HCCNSDX ASC
        ) AS rn
    FROM dbo.HCDIAGN WITH (NOLOCK)
    WHERE HCDXCOD IS NOT NULL AND LTRIM(RTRIM(HCDXCOD)) <> ''
) DX ON I.mptdoc = DX.HISTipDoc 
    AND LTRIM(RTRIM(I.mpcedu)) = DX.HISCKEY 
    AND I.IngCsc = DX.HISCSEC 
    AND DX.rn = 1
LEFT JOIN dbo.MAEDIA D WITH (NOLOCK) 
    ON D.dmcodi = COALESCE(NULLIF(LTRIM(RTRIM(DX.HCDXCOD)), ''), NULLIF(LTRIM(RTRIM(I.ingentdx)), ''));
```

## 4. Reglas y Lógica de Negocio

* **Homologación de Modalidad de Atención (`ClaPro`):** Se establece la equivalencia estricta para segmentar las atenciones operativas (`1` = Ambulatorio, `2` = Hospitalización, `3` = Urgencias, `4` = Tratamiento especial, `5` = Triage). El tablero se enfoca por defecto en los valores `3` y `5`.
* **Manejo de Fechas Centinelas:** El esquema aísla las fechas de egreso nulas o representadas como `1753-01-01`, catalogando dichos registros dinámicamente como el estado `ACTIVO / EN OBSERVACION`.
* **Asignación Física Asistencial:** Para pacientes en trámite de cama (`I.mpnumc` vacío) o atenciones ambulatorias en urgencias, el sistema imputa 'Sin Cama' o 'Consulta Externa' para garantizar su visibilidad en el tablero.
* **Cascada Diagnóstica (Zero-Inference):** El sistema prioriza el diagnóstico principal evolutivo de la historia clínica (`HCDIAGN`, donde `HCDXCLS = 1`). Si carece de registro clínico formal, recae en el diagnóstico primario de la admisión (`INGRESOS.ingentdx`).

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

* **Pacientes Activos Totales:** Conteo distintivo de pacientes con episodio abierto actualmente en el servicio.
  ```sql
  COUNT(DISTINCT CONSECUTIVO_INGRESO) WHERE ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION';
```
* **Días de Estancia (ALOS - Average Length of Stay):** Cálculo inclusivo (+1 día) aplicable a episodios egresados para evitar métricas nulas en atenciones menores a 24 horas.

```SQL
DATEDIFF(DAY, FECHA_INGRESO, FECHA_EGRESO) + 1
```
* Edad Dinámica al Ingreso:** Determinación de la edad cumplida en años mediante la diferencia exacta entre la fecha del evento y la fecha de nacimiento del paciente.

```SQL
DATEDIFF(YEAR, FECHA_NACIMIENTO, FECHA_INGRESO);
```
  
## 6. Consultas SQL por cada Chart

* **Chart 1:** Pacientes Activos en Urgencias (Big Number)

```SQL
SELECT COUNT(DISTINCT CONSECUTIVO_INGRESO) AS active_patients
FROM vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
WHERE TIPO_ATENCION = 'Urgencias' 
  AND ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION';
```  
* **Chart 2:** Matriz Operativa - Detalle de Pacientes Activos (Table Chart)

```SQL
SELECT 
  CONSECUTIVO_INGRESO, PACIENTE, EDAD_INGRESO, SERVICIO_INGRESO, 
  ESPECIALIDAD_TRATANTE, ASEGURADORA, DIAS_ESTANCIA, DIAGNOSTICO_PRINCIPAL
FROM vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
WHERE TIPO_ATENCION = 'Urgencias' 
  AND ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION'
ORDER BY FECHA_INGRESO ASC;
```
* **Chart 3:** Pacientes por Especialidad (Horizontal Bar Chart)

```SQL
SELECT 
  ESPECIALIDAD_TRATANTE, 
  COUNT(DISTINCT CONSECUTIVO_INGRESO) AS volume
FROM vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
WHERE TIPO_ATENCION = 'Urgencias' 
  AND ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION'
GROUP BY ESPECIALIDAD_TRATANTE
ORDER BY volume DESC;
```
* **Chart 4:** Pacientes por Área de Observación (Pie/Donut Chart)

```SQL
SELECT 
  SERVICIO_INGRESO, 
  COUNT(DISTINCT CONSECUTIVO_INGRESO) AS volume
FROM vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
WHERE TIPO_ATENCION = 'Urgencias' 
  AND ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION'
GROUP BY SERVICIO_INGRESO;
```
* **Chart 5:** Carga de Pacientes por Asegurador (Treemap)

```SQL
SELECT 
  ASEGURADORA, 
  COUNT(DISTINCT CONSECUTIVO_INGRESO) AS volume
FROM vw_CONSOLA_GESTION_INGRESOS_URGENCIAS
WHERE TIPO_ATENCION = 'Urgencias' 
  AND ESTADO_ATENCION = 'ACTIVO / EN OBSERVACION'
GROUP BY ASEGURADORA;
```

