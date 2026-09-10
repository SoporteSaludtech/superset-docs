# 18. Consola de Seguridad del Paciente (SOGCS)

---

## 1. Ficha Técnica General

* **Nombre del Tablero:** Consola de Seguridad del Paciente (SOGCS)
* **Plataforma Analítica:** IntelliHealth 6.1.0 (Apache Superset)
* **Sistema Origen:** Hosvital HIS (Microsoft SQL Server)
* **Módulo de Referencia:** Gestión de Calidad, Admisiones, Historia Clínica y Seguridad del Paciente
* **Frecuencia de Actualización:** Tiempo Real (Direct Query a vista transaccional optimizada)
* **Nivel de Acceso:** Dirección Médica, Comité de Calidad, Coordinadores SOGCS y Auditoría Concurrente

---

## 2. Propósito y Alcance

### 2.1 Propósito
Proveer una herramienta gerencial y operativa que permita centralizar la vigilancia epidemiológica, la tipificación de incidentes, cuasi fallas y eventos adversos bajo los lineamientos del Sistema Obligatorio de Garantía de Calidad en Salud (SOGCS). Facilita el análisis causal oportuno, la evaluación de la cultura de reporte y la trazabilidad documental para la toma de decisiones en los comités PAMEC (Plan de Mejoramiento Continuo).

### 2.2 Alcance
Abarca el monitoreo integral de todos los eventos notificados en las diferentes sedes e instalaciones de la institución, permitiendo segmentar por servicios asistenciales, perfiles profesionales, poblaciones vulnerables (gestantes y lactantes) y grados de criticidad (desde eventos centinela hasta cuasi fallas preventivas).

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en HOSVITAL HIS
* **`EVEADV`:** Tabla central de captura transaccional de eventos adversos e incidentes.
* **`INGRESOS`:** Tabla de hospitalización y admisiones para el cruce de fechas de ingreso y trazabilidad del paciente.
* **`MAESED`:** Maestra física de sedes de la institución.
* **`MAEPAB`:** Maestra de servicios asistenciales / pabellones.

### 3.2 DDL de la Vista Semántica Actualizada
{: .no-toc }
```sql
CREATE OR ALTER VIEW VW_SEGURIDAD_PACIENTE_EVENTOS AS
SELECT 
    ev.MPCedu AS Documento_Paciente,
    ev.MPTDoc AS Tipo_Documento,
    ev.EVEADVSEC AS Secuencia_Evento,
    ev.EVEADving AS Id_Ingreso,
    i.IngFecAdm AS Fecha_Ingreso_Paciente,
    ev.EVEADVFEC AS Fecha_Ocurrencia,
    ev.EVEADVREP AS Fecha_Reporte,
    DATEDIFF(hour, ev.EVEADVFEC, ev.EVEADVREP) AS Horas_Hasta_Reporte,
    ev.EVEADVSED AS Codigo_Sede,
    ISNULL(s.MCDnom, 'SEDE PRINCIPAL') AS Nombre_Sede,
    ev.EVEADVSER AS Codigo_Servicio,
    ISNULL(p.mpnomp, 'SERVICIO GENERAL') AS Nombre_Servicio,
    CASE UPPER(LTRIM(RTRIM(ev.EVEADVGES))) WHEN 'S' THEN 'Sí' WHEN 'SI' THEN 'Sí' ELSE 'No' END AS Es_Gestante,
    CASE UPPER(LTRIM(RTRIM(ev.EVEADVLAC))) WHEN 'S' THEN 'Sí' WHEN 'SI' THEN 'Sí' ELSE 'No' END AS Es_Lactante,
    CASE UPPER(LTRIM(RTRIM(ev.EVEADVANO))) WHEN 'S' THEN 'Anónimo' WHEN 'N' THEN 'Identificado' ELSE 'Identificado' END AS Tipo_Reporte_Anonimo,
    ev.EPCCON AS Codigo_Programa_Clasificacion,
    CASE UPPER(LTRIM(RTRIM(ev.EPCCON)))
        WHEN '1' THEN 'Evento No Serio'
        WHEN '2' THEN 'Evento Serio'
        WHEN '3' THEN 'Evento Centinela'
        WHEN '4' THEN 'Cuasi Falla' ELSE 'OTRA CLASIFICACIÓN' END AS Descripcion_Programa_Clasificacion,
    ev.EVEGRUSEC AS Grupo_Evento_Codigo,
    CASE UPPER(LTRIM(RTRIM(ev.EVEGRUSEC)))
        WHEN '1' THEN 'Identificación del evento adverso'
        WHEN '2' THEN 'Notificación del evento adverso'
        WHEN '3' THEN 'Investigación del evento adverso'
        WHEN '4' THEN 'Análisis del Evento Adverso'
        WHEN '5' THEN 'Prevención evento adverso' ELSE 'OTRO GRUPO' END AS Grupo_Evento_Descripcion,
    ev.EVESUBSEC AS Subgrupo_Evento_Codigo,
    CASE 
        WHEN ev.EVEGRUSEC = '1' AND ev.EVESUBSEC = '1' THEN 'Alerta o señal'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '1' THEN 'Definitiva (Certain)'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '2' THEN 'Probable (Likely)'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '3' THEN 'Posible (Possible)'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '4' THEN 'Improbable (Unlikely)'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '5' THEN 'Condicional / No Clasificado'
        WHEN ev.EVEGRUSEC = '2' AND ev.EVESUBSEC = '6' THEN 'No Evaluable / Inclasificable'
        WHEN ev.EVEGRUSEC = '3' AND ev.EVESUBSEC = '1' THEN 'Manual del Investigador'
        WHEN ev.EVEGRUSEC = '3' AND ev.EVESUBSEC = '2' THEN 'Organización de Investigación por Contrato (OIC)'
        WHEN ev.EVEGRUSEC = '3' AND ev.EVESUBSEC = '3' THEN 'Patrocinador'
        WHEN ev.EVEGRUSEC = '4' AND ev.EVESUBSEC = '1' THEN 'Factor Científico'
        WHEN ev.EVEGRUSEC = '4' AND ev.EVESUBSEC = '2' THEN 'Factor Percibido'
        WHEN ev.EVEGRUSEC = '4' AND ev.EVESUBSEC = '3' THEN 'Factor Institucional o corporativo'
        WHEN ev.EVEGRUSEC = '5' AND ev.EVESUBSEC = '1' THEN 'Riesgo de caídas'
        WHEN ev.EVEGRUSEC = '5' AND ev.EVESUBSEC = '2' THEN 'Riesgo de úlceras de Presión'
        WHEN ev.EVEGRUSEC = '5' AND ev.EVESUBSEC = '3' THEN 'Riesgo de Errores de Medicación'
        ELSE 'SUBGRUPO GENERAL' END AS Subgrupo_Evento_Descripcion,
    ev.EVEADVPER AS Perfil_Profesional_Reporta,
    RTRIM(ev.EVEADVDES) AS Descripcion_Evento,
    RTRIM(ev.EVEADVPOS) AS Posibles_Causas,
    ev.EVEADVEST AS Estado_Codigo
FROM EVEADV ev WITH (NOLOCK)
OUTER APPLY (SELECT TOP 1 IngFecAdm FROM INGRESOS WITH (NOLOCK) WHERE IngCsc = ev.EVEADving) i
OUTER APPLY (SELECT TOP 1 MCDnom FROM MAESED WITH (NOLOCK) WHERE RTRIM(MCDpto) = RTRIM(ev.EVEADVSED)) s
OUTER APPLY (SELECT TOP 1 mpnomp FROM MAEPAB WITH (NOLOCK) WHERE RTRIM(mpclapro) = RTRIM(ev.EVEADVSER)) p;
```
---

## 4. Reglas y Lógica de Negocio

El diseño semántico y analítico de la consola responde a los estándares normativos del **Sistema Obligatorio de Garantía de Calidad en Salud (SOGCS)** y a la metodología del **Protocolo de Londres** para la gestión del riesgo clínico:

* **Tiempos de Notificación y Oportunidad:**
    * El lapso de respuesta se calcula midiendo la diferencia temporal en horas transcurridas entre el momento del suceso y su ingreso formal al sistema:
      $\Delta t = \text{Fecha\_Reporte} - \text{Fecha\_Ocurrencia}$
    * Facilita la auditoría del cumplimiento de la política de notificación institucional ($\le 24 \text{ horas}$), reduciendo el sesgo de memoria del personal y garantizando la contención oportuna del riesgo clínico.
* **Evaluación de Cultura Justa y No Punitiva:**
    * La segregación de la variable `Tipo_Reporte_Anonimo` (`EVEADVANO`) permite calcular el índice de confianza institucional. Un predominio de reportes identificados refleja madurez en la cultura de seguridad, mientras que una alta tasa de anonimato orienta intervenciones pedagógicas frente al temor a represalias.
* **Taxonomía SOGCS y Severidad del Evento:**
    * Homologación de la codificación `EPCCON` en cuatro cuadrantes clínicos:
        1. **Cuasi Falla (Near Miss):** Error que no alcanzó al paciente gracias a barreras de seguridad. Constituye el pilar del análisis proactivo.
        2. **Evento No Serio:** Incidente que alcanzó al paciente pero no generó secuelas ni prolongó la estancia.
        3. **Evento Serio:** Evento no intencional con daño temporal o prolongación de estancia hospitalaria.
        4. **Evento Centinela:** Suceso adverso crítico que causa muerte o pérdida funcional permanente, requiriendo activación inmediata del comité de seguridad en menos de 72 horas.
* **Trazabilidad Causal (Grupos y Subgrupos):**
    * Clasificación jerárquica estandarizada en Hosvital HIS donde el **Grupo 4 (Análisis del Evento Adverso)** aísla específicamente los factores etiológicos: *Factores Científicos*, *Factores Percibidos* y *Factores Institucionales/Corporativos*.
---

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

$$\begin{aligned} \textbf{Total Incidentes/Eventos} &= \sum_{i=1}^{N} \mathbf{1}_{(\text{Secuencia\_Evento}_i)} \\ \textbf{Oportunidad Promedio (Horas)} &= \frac{1}{N} \sum_{i=1}^{N} \text{DATEDIFF}(\text{hour}, \text{Fecha\_Ocurrencia}_i, \text{Fecha\_Reporte}_i) \\ \textbf{Casos Críticos (Serio + Centinela)} &= \sum_{i=1}^{N} \mathbf{1}_{\{\text{Codigo\_Programa\_Clasificacion}_i \in (2, 3)\}} \\ \textbf{Índice de Cuasi Fallas Preventivas} &= \frac{\sum \mathbf{1}_{\{\text{Clasificacion} = \text{'Cuasi Falla'}\}}}{\text{Total Reportes}} \times 100 \end{aligned}$$

### 5.2 Matriz de Definición de Indicadores

| Indicador | Dimensión / Expresión Técnica | Interpretación Clínica / PAMEC | Meta / Umbral |
| :--- | :--- | :--- | :--- |
| **Volumen Total** | `COUNT(Secuencia_Evento)` | Medición global de la tasa de notificación institucional. | Tendencia ascendente controlada |
| **Oportunidad de Reporte** | `AVG(Horas_Hasta_Reporte)` | Velocidad de notificación tras el suceso. | $\le 24 \text{ horas}$ |
| **Carga de Severidad Crítica** | `COUNT() WHERE EPCCON IN ('2', '3')` | Eventos con potencial impacto legal y asistencial grave. | $0 \text{ Centinelas}$ |
| **Eficacia de Barreras** | `COUNT() WHERE EPCCON = '4'` | Detección preventiva antes de que el error vulnere al paciente. | $\ge 20\%$ del volumen global |

---

## 6. Consultas SQL por cada Chart

### 6.1 Tarjetas Ejecutivas de Cabecera (KPI Cards)

* **KPI 1: Total de Reportes Registrados**
```sql
  SELECT 
      COUNT(Secuencia_Evento) AS Total_Reportes
  FROM VW_SEGURIDAD_PACIENTE_EVENTOS;
```
* **KPI 2: Oportunidad Promedio de Notificación**
```SQL
SELECT 
    CAST(ROUND(AVG(CAST(Horas_Hasta_Reporte AS FLOAT)), 1) AS NUMERIC(10,1)) AS Promedio_Horas_Reporte
FROM VW_SEGURIDAD_PACIENTE_EVENTOS;
```
* **KPI 3: Consolidado de Eventos Críticos (Serios y Centinelas)**
```SQL
SELECT 
    COUNT(Secuencia_Evento) AS Total_Eventos_Criticos
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
WHERE Codigo_Programa_Clasificacion IN ('2', '3');
```
* **KPI 4: Detección de Cuasi Fallas**
```SQL
SELECT 
    COUNT(Secuencia_Evento) AS Total_Cuasi_Fallas
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
WHERE Codigo_Programa_Clasificacion = '4';
```
* KPI 5: Distribución en Población Gestante**
```SQL
SELECT 
    Es_Gestante,
    COUNT(Secuencia_Evento) AS Total_Casos
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
GROUP BY Es_Gestante;
```
* **KPI 6: Cultura de Seguridad - Reporte Anónimo vs Identificado**
```SQL
SELECT 
    Tipo_Reporte_Anonimo,
    COUNT(Secuencia_Evento) AS Total_Reportes
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
GROUP BY Tipo_Reporte_Anonimo;
```
* **KPI 7: Top 10 Servicios por Frecuencia de Eventos**
```SQL
SELECT TOP 10 
    Nombre_Servicio,
    COUNT(Secuencia_Evento) AS Total_Eventos
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
GROUP BY Nombre_Servicio
ORDER BY Total_Eventos DESC;
```
* **KPI 8: Grupos y Subgrupos de Riesgo**
```SQL
SELECT 
    Grupo_Evento_Descripcion,
    Subgrupo_Evento_Descripcion,
    COUNT(Secuencia_Evento) AS Total_Incidentes
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
GROUP BY Grupo_Evento_Descripcion, Subgrupo_Evento_Descripcion;
```
* **KPI 9: Análisis de Factores Causales SOGCS**
```SQL
SELECT 
    Subgrupo_Evento_Descripcion AS Factor_Causal,
    COUNT(Secuencia_Evento) AS Frecuencia
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
WHERE Grupo_Evento_Codigo = '4'
GROUP BY Subgrupo_Evento_Descripcion
ORDER BY Frecuencia DESC;
```
* **KPI 10: Mapa de Calor de Eventos: Sede vs Servicio**
```SQL
SELECT 
    Nombre_Sede,
    Nombre_Servicio,
    COUNT(Secuencia_Evento) AS Eventos_Registrados
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
GROUP BY Nombre_Sede, Nombre_Servicio;
```
* **KPI 11: Registro Detallado de Eventos Adversos y Trazabilidad (Sábana Operativa / Tabla de Registros Crudos)**
```SQL
SELECT 
    Fecha_Ocurrencia,
    Secuencia_Evento AS ID_Evento,
    Nombre_Sede,
    Nombre_Servicio,
    Descripcion_Programa_Clasificacion AS Clasificacion,
    Subgrupo_Evento_Descripcion AS Tipologia,
    Tipo_Reporte_Anonimo AS Modalidad,
    Descripcion_Evento,
    Posibles_Causas
FROM VW_SEGURIDAD_PACIENTE_EVENTOS
ORDER BY Fecha_Ocurrencia DESC;
```
## 7. Estructura y Configuración del Dashboard (IntelliHealth 6.1.0)

### 7.1 Esquema de Distribución en Grilla (Grid 12-Column Standard)

El tablero se encuentra estructurado bajo un diseño modular de 12 columnas en IntelliHealth, optimizado para garantizar una lectura jerárquica desde los indicadores ejecutivos gerenciales hasta el detalle analítico operativo:

| Fila / Nivel | Componentes Visuales y Tipo de Chart | Distribución en Grilla |
| :--- | :--- | :--- |
| **Fila 1** | **Filtros Nativos Globales:** Rango de Fechas, Sede, Servicio, Clasificación del Evento y Tipo de Reporte. | `Disposición Horizontal (Full Width)` |
| **Fila 2** | **Tarjetas KPI Ejecutivas:** Total de Reportes, Promedio de Oportunidad, Eventos Críticos y Cuasi Fallas. | 4 Tarjetas de `Col: 3` c/u |
| **Fila 3** | **Epidemiología y Cultura:** Distribución en Gestantes (Pie), Modalidad Anónima vs. Identificada (Donut) y Top 10 Servicios Afectados (Barra Horizontal). | Dos gráficos de `Col: 3` y un gráfico de `Col: 6` |
| **Fila 4** | **Matriz de Riesgos SOGCS:** Jerarquía de Grupos/Subgrupos (Treemap), Análisis de Factores Causales (Barras) y Mapa de Calor (Sede vs. Servicio). | Treemap de `Col: 6`, Barras y Heatmap de `Col: 3` c/u |
| **Fila 5** | **Trazabilidad y Auditoría:** Sábana Operativa de Registros Crudos con formato condicional y soporte de exportación. | Tabla Completa de `Col: 12` |

---

### 7.2 Detalle de Configuración y Paleta Institucional (JSON Metadata)

La consola incorpora interactividad bidireccional mediante `cross_filters_enabled`, permitiendo al usuario filtrar dinámicamente todo el tablero con un solo clic sobre cualquier segmento visual. 

La asignación cromática de las etiquetas y la orientación de los filtros se encuentran centralizadas a través del siguiente esquema en formato JSON Metadata:

```json
{
  "label_colors": {
    "Evento Centinela": "#E04355",
    "Evento Serio": "#FF9900",
    "Evento No Serio": "#FCCC4F",
    "Cuasi Falla": "#269A99",
    "Sí": "#E04355",
    "No": "#269A99",
    "Anónimo": "#6C757D",
    "Identificado": "#1A85FF"
  },
  "cross_filters_enabled": true,
  "filter_bar_orientation": "HORIZONTAL"
}
```