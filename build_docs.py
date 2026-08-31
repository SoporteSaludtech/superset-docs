import os

# Crear directorio de dashboards
os.makedirs("docs/dashboards", exist_ok=True)

# 1. mkdocs.yml
mkdocs_content = """site_name: Centro de Analítica e Inteligencia Clínica - Hosvital HIS
site_url: https://soportesaludtech.github.io/superset-docs/
site_description: Repositorio técnico, funcional y normativo de indicadores de gestión clínica y financiera.
site_author: Dirección de Analítica y Soluciones en Salud

theme:
  name: material
  language: es
  palette:
    - scheme: default
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-7
        name: Modo Oscuro
    - scheme: slate
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-4
        name: Modo Claro
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.arithmatex:
      generic: true
  - tables
  - attr_list

extra_javascript:
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

nav:
  - Marco General: index.md
  - Gestión Asistencial:
      - Egresos y Urgencias: dashboards/01-egresos-urgencias.md
      - Calidad e IAAS: dashboards/04-vigilancia-iaas.md
  - Gestión Financiera:
      - Prefacturación y Producción: dashboards/02-prefacturacion.md
  - Gestión Quirúrgica:
      - Ocupación y Programación QX: dashboards/03-ordenes-quirurgicas.md
"""

# 2. docs/index.md
index_content = """# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio central de documentación técnica, operativa y funcional de los cuadros de mando institucionales orientados al monitoreo del ciclo asistencial, la optimización financiera y la seguridad del paciente.

---

## Matriz General de Cuadros de Mando

| Área de Gestión | Cuadro de Mando | Indicadores Principales | Frecuencia | Enlace al Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Gestión Asistencial** | **Egresos y Urgencias** | Estancia Media (ALOS), Tasa de Ocupación, Rotación de Camas | 15 Minutos | [Ver Ficha Técnica](dashboards/01-egresos-urgencias.md) |
| **Gestión Asistencial** | **Calidad, Seguridad e IAAS** | Tasa de Infecciones x 100 Camas-Día, Aislamiento por Pabellón | 15 Minutos | [Ver Ficha Técnica](dashboards/04-vigilancia-iaas.md) |
| **Gestión Financiera** | **Prefacturación y Producción** | Valor WIP en Tránsito, Aging de Prefactura, Consumos por EPS | 10 Minutos | [Ver Ficha Técnica](dashboards/02-prefacturacion.md) |
| **Gestión Quirúrgica** | **Programación y Ocupación QX** | Tasa de Cancelación, Oportunidad Quirúrgica, Demanda por Especialidad | 5 Minutos | [Ver Ficha Técnica](dashboards/03-ordenes-quirurgicas.md) |

---

## Flujo del Modelo de Información

=== "1. Capa Transaccional (Origen)"
    **Hosvital HIS - Motor Relacional SQL Server**
    
    * **Entidades Principales:** `Ingresos`, `Capbas`, `TMPFAC`, `procir`, `HCDIAGN`, `MAEDIA`.
    * **Naturaleza del Dato:** Registro transaccional en tiempo real derivado de la operación clínica, admisión de pacientes, programación quirúrgica y facturación médica.

=== "2. Capa de Transformación y Reglas"
    **Ingeniería de Datos y Consultas T-SQL**
    
    * **Tratamiento de Fechas:** Aislamiento de valores centinela por omisión (`<= 1753-01-01`).
    * **Filtros de Integridad:** Depuración de anulación de cargos (`tfestaanu = 'N'`) y trazabilidad de cancelaciones (`PFcHrCnc`).
    * **Métricas Asistenciales:** Cálculo dinámico de estancias acumuladas, rangos etarios quinquenales y consolidación multirubro.

=== "3. Capa de Explotación y Decisión"
    **Consolas Analíticas e Indicadores Institucionales**
    
    * **Tarjetas KPI y Resúmenes:** Resumen consolidado para la toma de decisiones directivas.
    * **Visualización Segmentada:** Distribución por asegurador (EPS), pabellón y especialidad médica.
    * **Consolas Nominales:** Tablas de auditoría caso a caso para comités de calidad y jefaturas asistenciales.

---

## Estándares de Calidad y Gobierno del Dato

!!! info "Tratamiento de Valores Nulos y Fechas Centinela"
    Todas las consultas aíslan fechas no registradas (`<= 1753-01-01`) para evitar distorsiones en los promedios de estancia (ALOS), oportunidad en triage y programación quirúrgica.

!!! success "Integridad de Transacciones Asistenciales y Financieras"
    Se aplican criterios estrictos de no anulación en los consumos clínicos (`TMPFAC1.tfestaanu1 = 'N'` y `TMPFAC2.TFestaanu2 = 'N'`), garantizando que solo la producción real sea considerada en los balances de prefacturación.

!!! warning "Seguridad, Perfiles y Confidencialidad"
    La información clínica sensible se encuentra protegida bajo políticas de gobierno del dato, permitiendo el acceso a las vistas de auditoría únicamente a los roles correspondientes (Dirección Médica, Coordinación de Quirófanos, Auditoría de Cuentas y Comité de Infecciones).
"""

# 3. docs/dashboards/01-egresos-urgencias.md
d1_content = """# Gestión Asistencial: Egresos Hospitalarios y Urgencias

- **Módulo de Origen:** Hospitalización y Urgencias (`Ingresos`, `Capbas`, `Maepab`)
- **Propósito:** Monitorizar el flujo de pacientes, la oportunidad de alta y la disponibilidad de camas operativas.
- **Frecuencia de Actualización:** 15 minutos

---

## 1. Alcance Conceptual y Fórmulas Matemáticas

### Estancia Media Hospitalaria (ALOS - Average Length of Stay)
Mide el promedio de días que un paciente permanece internado desde su ingreso formal hasta el egreso médico:

$$\\text{ALOS (Días)} = \\frac{\\sum_{i=1}^{n} (\\text{FechaEgreso}_i - \\text{FechaIngreso}_i)}{\\text{Total Egresos}}$$

### Tasa de Ocupación Hospitalaria
Porcentaje de utilización de la capacidad instalada en un periodo determinado:

$$\\text{Ocupación (\\%)} = \\left( \\frac{\\text{Camas Ocupadas}}{\\text{Camas Habilitadas}} \\right) \\times 100$$

### Criterios de Interpretación Clínica y Operativa
- **Ocupación 75% - 85%:** Rango óptimo de operación institucional que permite absorber fluctuaciones de demanda sin saturar urgencias.
- **Ocupación > 90%:** Alerta crítica de congestión hospitalaria. Se incrementa el riesgo de retención de pacientes en urgencias (*boarding*).
- **Estancia Prolongada (> 1.5 DE del promedio por patología):** Requiere intervención de auditoría médica para identificar cuellos de botella en interconsultas, imágenes diagnósticas o trámite de contrarreferencia.

---

## 2. Especificación Técnica T-SQL

```sql
SELECT 
    i.IngCsc AS CONSECUTIVO_INGRESO,
    i.MPCedu AS NUMERO_IDENTIFICACION,
    i.MPTDoc AS TIPO_IDENTIFICACION,
    c.MPNomC AS NOMBRE_PACIENTE,
    i.IngFecAdm AS FECHA_INGRESO,
    i.IngFecEgr AS FECHA_EGRESO,
    CASE 
        WHEN i.ClaPro = 2 THEN 'Hospitalización'
        WHEN i.ClaPro = 3 THEN 'Urgencias'
        ELSE 'Otro'
    END AS TIPO_ATENCION,
    pab.MPNomP AS SERVICIO_EGRESO,
    i.IngCam AS CAMA_EGRESO,
    esp.MENOME AS ESPECIALIDAD_MEDICO_TRATANTE,
    med.mmnomm AS MEDICO_TRATANTE,
    emp.MENOMB AS CONTRATO_EMPRESA,
    CASE 
        WHEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) >= 0 
        THEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) + 1 
        ELSE 1 
    END AS DIAS_ESTANCIA
FROM dbo.Ingresos i
INNER JOIN dbo.Capbas c ON i.MPCedu = c.MPCedu AND i.MPTDoc = c.MPTDoc
LEFT JOIN dbo.Maepab pab ON i.MPCodP = pab.MPCodP
LEFT JOIN dbo.Maemed1 med ON i.IngMedTra = med.mmcodm
LEFT JOIN dbo.MAEESP esp ON med.mmeesp = esp.mecode
LEFT JOIN dbo.Maeemp emp ON i.IngNit = emp.MENNIT
WHERE i.ClaPro IN (2, 3)
  AND i.IngFecEgr IS NOT NULL 
  AND i.IngFecEgr > '1753-01-01';
3. Diccionario de Componentes VisualesComponenteTipo de VisualizaciónMétrica / DimensiónObjetivo OperativoTotal EgresosMétrica Resumen (KPI)COUNT(CONSECUTIVO_INGRESO)Volumen de altas efectivas en el corte.Promedio EstanciaMétrica Resumen (KPI)AVG(DIAS_ESTANCIA)Control del giro de cama asistencial.Egresos por EspecialidadGráfico de BarrasESPECIALIDAD_MEDICO_TRATANTECarga resolutiva por equipo médico.Distribución por PabellónGráfico Circular (Donut)SERVICIO_EGRESOConcentración de altas por servicio.Consola Nominal de EgresosTabla InteractivaPaciente, Cama, Fechas, AseguradorAuditoría caso a caso y revisión de estancia."""4. docs/dashboards/02-prefacturacion.mdd2_content = """# Gestión Financiera: Prefacturación y Producción AsistencialMódulo de Origen: Facturación / Cuentas Médicas (TMPFAC, TMPFAC1, TMPFAC2)Propósito: Supervisar los consumos clínicos en tránsito para evitar la extemporaneidad y optimizar la radicación fiscal.Frecuencia de Actualización: 10 minutos1. Alcance Conceptual y Fórmulas MatemáticasValor Total Prefacturado (WIP - Work in Progress Financiero)Cuantifica la producción asistencial ejecutada y cargada a la admisión del paciente que aún no cuenta con factura física radicada:$$\text{Total Prefacturado (\\$)} = \sum (\text{Cantidad} \times \text{Valor Unitario})$$Días de Rezago en Cierre de Cuenta (Aging)Tiempo transcurrido desde el egreso del paciente hasta la liquidación de la orden de facturación:$$\text{Aging (Días)} = \text{Fecha Actual} - \text{Fecha de Egreso}$$Criterios de Interpretación FinancieraAging <= 3 días: Operación estándar de auditoría concurrente y liquidación oportuna.Aging 4 - 7 días: Alerta operativa por cargos pendientes (evoluciones médicas, notas de enfermería o despacho de farmacia sin cerrar).Aging > 7 días: Riesgo severo de glosa por radicación extemporánea y retraso en el flujo de caja.2. Especificación Técnica T-SQLSQLSELECT 
    Nombre_Empresa AS CONTRATO_EMPRESA,
    fecha_ingreso AS FECHA_INGRESO,
    hora_ingreso AS HORA_INGRESO,
    identificacion AS NUMERO_IDENTIFICACION,
    tipo_id AS TIPO_IDENTIFICACION,
    Nombre_Paciente AS NOMBRE_PACIENTE,
    [#Ingreso] AS CONSECUTIVO_INGRESO,
    Tipo_Rubro AS TIPO_RUBRO,
    SUM(Valor) AS TOTAL_VALOR
FROM (
    SELECT 
        M.MenomB AS Nombre_Empresa,
        T.TFFCHI AS fecha_ingreso, 
        T.tfhori AS hora_ingreso, 
        T.tfcedu AS identificacion, 
        T.tftdoc AS tipo_id, 
        LTRIM(RTRIM(ISNULL(C.mpnom1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpnom2, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape2, ''))) AS Nombre_Paciente,
        T.Tmctving AS [#Ingreso],
        'Procedimientos' AS Tipo_Rubro,
        ISNULL(T1.tfvatp, 0) AS Valor
    FROM dbo.TMPFAC T
    INNER JOIN dbo.TMPFAC1 T1 
        ON T.tfcedu = T1.tfcedu AND T.Tftdoc = T1.Tftdoc AND T.Tmctving = T1.Tmctving
    INNER JOIN dbo.MAEEMP M ON T1.tfnitp = M.mennit
    INNER JOIN dbo.CAPBAS C ON T.tfcedu = C.mpcedu AND T.tftdoc = C.mptdoc
    WHERE T1.tfestaanu1 = 'N'

    UNION ALL

    SELECT 
        M.MenomB AS Nombre_Empresa,
        T.TFFCHI AS fecha_ingreso, 
        T.tfhori AS hora_ingreso, 
        T.tfcedu AS identificacion, 
        T.tftdoc AS tipo_id, 
        LTRIM(RTRIM(ISNULL(C.mpnom1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpnom2, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape2, ''))) AS Nombre_Paciente,
        T.Tmctving AS [#Ingreso],
        'Suministros y Medicamentos' AS Tipo_Rubro,
        ISNULL(T2.tfvats, 0) AS Valor
    FROM dbo.TMPFAC T
    INNER JOIN dbo.TMPFAC2 T2 
        ON T.tfcedu = T2.tfcedu AND T.Tftdoc = T2.Tftdoc AND T.Tmctving = T2.Tmctving
    INNER JOIN dbo.MAEEMP M ON T2.tfnitS = M.mennit
    INNER JOIN dbo.CAPBAS C ON T.tfcedu = C.mpcedu AND T.tftdoc = C.mptdoc
    WHERE T2.TFestaanu2 = 'N' AND T2.TFSTpotrn = 'F'
) AS Consolidado
GROUP BY 
    Nombre_Empresa, fecha_ingreso, hora_ingreso, 
    identificacion, tipo_id, Nombre_Paciente, [#Ingreso], Tipo_Rubro;
3. Diccionario de Componentes VisualesComponenteTipo de VisualizaciónMétrica / DimensiónObjetivo OperativoTotal PrefacturadoMétrica Resumen (KPI)SUM(TOTAL_VALOR)Monto acumulado en cuentas abiertas.Cuentas en ProcesoMétrica Resumen (KPI)COUNT(DISTINCT CONSECUTIVO_INGRESO)Carga total de admisiones pendientes.Proporción de RubrosGráfico Circular (Donut)TIPO_RUBRORelación de gasto Procedimientos vs Medicamentos.Top Aseguradores (EPS)Gráfico de BarrasCONTRATO_EMPRESAIdentificación de concentración de cartera WIP.Consola de AuditoríaTabla InteractivaPaciente, Ingreso, Rubros, MontosTrazabilidad de admisiones listas para facturar."""5. docs/dashboards/03-ordenes-quirurgicas.mdd3_content = """# Gestión Quirúrgica: Ocupación y Programación de SalasMódulo de Origen: Bloque Quirúrgico (procir, procir1, HCCOM1)Propósito: Trazabilidad integral de las solicitudes de cirugía, confirmaciones de tabla y efectividad en el uso de quirófanos.Frecuencia de Actualización: 5 minutos1. Alcance Conceptual y Fórmulas MatemáticasTasa de Cancelación QuirúrgicaProporción de cirugías reservadas/confirmadas que fueron suspendidas antes o durante el acto quirúrgico:$$\text{Tasa Cancelación (\\%)} = \left( \frac{\text{Órdenes Canceladas}}{\text{Total Órdenes Programadas}} \right) \times 100$$Tasa de Cumplimiento de Tabla QuirúrgicaEfectividad en la ejecución del plan operatorio programado:$$\text{Cumplimiento (\\%)} = \left( \frac{\text{Cirugías Realizadas}}{\text{Total Órdenes Programadas}} \right) \times 100$$Criterios de Interpretación QuirúrgicaCancelación <= 3%: Estándar de excelencia operativa y adecuada preparación prequirúrgica.Cancelación > 5%: Oportunidad de intervención en confirmación telefónica, disponibilidad de instrumental o valoración preanestésica.2. Especificación Técnica T-SQLSQLSELECT DISTINCT 
    PC.ProFSep AS FECHA_SOLICITUD,
    PC.procircod AS NUMERO_ORDEN,
    PC.profecF AS FECHA_PROGRAMADA_CIRUGIA,
    CONCAT(CONVERT(VARCHAR, PC.profecF, 103), ' ', PC.ProHorI, ' - ', PC.ProHorF) AS HORARIO_CIRUGIA,
    PC.PfcHrCnf AS FECHA_CONFIRMACION,
    PC.PFcHrCnc AS FECHA_CANCELACION,
    CASE 
        WHEN PC.PFcHrCnc IS NULL OR PC.PFcHrCnc <= '17530101' THEN 'No Cancelada' 
        ELSE 'Cancelada' 
    END AS ESTADO_CANCELACION,
    CB.mpcedu AS NUMERO_DOCUMENTO,
    CB.mptdoc AS TIPO_DOCUMENTO,
    CB.mpnomc AS NOMBRE_PACIENTE,
    CB.mptele AS TELEFONO_PACIENTE,
    ISNULL(PC1.Crgcod, 'N/A') AS CUPS_PROCEDIMIENTO,
    ISNULL(MP.prnomb, 'PROCEDIMIENTO SIN DEFINIR') AS DESCRIPCION_PROCEDIMIENTO,
    ME.MENOME AS ESPECIALIDAD_QX,
    M1.mmnomm AS MEDICO_ORDENANTE,
    CASE 
        WHEN CAST(PC.ProFliSol AS VARCHAR) = '0' THEN 'Sin definir' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '1' THEN 'Orden Ambulatoria' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '2' THEN 'Orden Hospitalización' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '3' THEN 'Orden Urgencias' 
        ELSE 'Otro' 
    END AS ORIGEN_ATENCION,
    CASE 
        WHEN CAST(PC.proesta AS VARCHAR) = '1' THEN 'Reservada'
        WHEN CAST(PC.proesta AS VARCHAR) = '2' THEN 'Confirmada'
        WHEN CAST(PC.proesta AS VARCHAR) = '3' THEN 'Cancelada'
        WHEN CAST(PC.proesta AS VARCHAR) = '4' THEN 'Realizada'
        ELSE 'Pendiente' 
    END AS ESTADO_ORDEN
FROM dbo.procir PC
LEFT JOIN dbo.procir1 PC1 
    ON PC.proempcod = PC1.proempcod AND PC.proMcdpto = PC1.proMcdpto AND PC.procircod = PC1.procircod
LEFT JOIN dbo.MAEESP ME ON RTRIM(PC.ProEspSep) = RTRIM(ME.mecode)
LEFT JOIN dbo.capbas CB ON PC.mpcedu = CB.mpcedu AND PC.mptdoc = CB.mptdoc
LEFT JOIN dbo.maepro MP ON PC1.Crgcod = MP.prcodi
LEFT JOIN dbo.maemed1 M1 ON PC.propersep = M1.mmcodm
LEFT JOIN dbo.HCCOM1 HC 
    ON PC.mpcedu = HC.HISCKEY AND PC.mptdoc = HC.HISTIPDOC AND PC.ProFliSol = HC.hiscsec;
3. Diccionario de Componentes VisualesComponenteTipo de VisualizaciónMétrica / DimensiónObjetivo OperativoTotal Solicitudes QXMétrica Resumen (KPI)COUNT(DISTINCT NUMERO_ORDEN)Demanda global quirúrgica.Cirugías RealizadasMétrica Resumen (KPI)COUNT(DISTINCT NUMERO_ORDEN) ejecutadasProductividad efectiva de quirófanos.Estado de la ProgramaciónGráfico Circular (Donut)ESTADO_ORDENProporción Reservadas vs Confirmadas vs Canceladas.Demanda por EspecialidadGráfico de BarrasESPECIALIDAD_QXCarga de procedimientos por servicio quirúrgico.Consola de ProgramaciónTabla InteractivaPaciente, CUPS, Cirujano, TeléfonoHerramienta de gestión para confirmación de tabla."""6. docs/dashboards/04-vigilancia-iaas.mdd4_content = """# Gestión de Calidad: Vigilancia Epidemiológica e IAASMódulo de Origen: Historia Clínica / Diagnósticos (HCDIAGN, MAEDIA, HCCOM1)Propósito: Detección, aislamiento y seguimiento de infecciones asociadas a la atención en salud (IAAS) y patologías de notificación epidemiológica.Frecuencia de Actualización: 15 minutos1. Alcance Conceptual y Fórmulas MatemáticasÍndice de Carga Infecciosa por 100 Camas-DíaMide la presión epidemiológica intrahospitalaria normalizada por los días de internación acumulados:$$\text{Índice IAAS} = \left( \frac{\text{Total Pacientes con Infección Activa}}{\sum \text{Días de Estancia Acumulados}} \right) \times 100$$Criterios de Interpretación EpidemiológicaÍndice <= 3.0% (Controlado): Comportamiento dentro de los límites de control institucional.Índice > 3.0% (Alerta de Brote): Requiere activación inmediata de rondas de bioseguridad, tipificación microbiológica y desinfección terminal.2. Especificación Técnica T-SQLSQLSELECT 
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
WHERE (hc.HCDXCOD LIKE 'A%' OR hc.HCDXCOD LIKE 'B%' OR hc.HCDXCOD LIKE 'J0%' OR hc.HCDXCOD LIKE 'J1%' OR hc.HCDXCOD LIKE 'N390%');
3. Diccionario de Componentes VisualesComponenteTipo de VisualizaciónMétrica / DimensiónObjetivo OperativoÍndice IAASMétrica Resumen (KPI)(COUNT(DISTINCT ID)*100.0) / NULLIF(SUM(ESTANCIA), 0)Presión infecciosa sobre camas ocupadas.Matriz Térmica (Heatmap)Mapa de CalorDiagnóstico CIE-10 vs Grupo EtarioIdentificación de poblaciones vulnerables.Aislamientos por PabellónGráfico Circular (Donut)SERVICIO_ACTUALDistribución de carga de bioseguridad.Consola EpidemiológicaTabla InteractivaPaciente, CIE-10, Estancia, PabellónHerramienta de ronda para Comité de Infecciones."""files = {"mkdocs.yml": mkdocs_content,"docs/index.md": index_content,"docs/dashboards/01-egresos-urgencias.md": d1_content,"docs/dashboards/02-prefacturacion.md": d2_content,"docs/dashboards/03-ordenes-quirurgicas.md": d3_content,"docs/dashboards/04-vigilancia-iaas.md": d4_content,}for path, content in files.items():with open(path, "w", encoding="utf-8") as f:f.write(content.strip())print(f"Generado: {path}")print("\n--- Todos los archivos han sido generados exitosamente en UTF-8 ---")