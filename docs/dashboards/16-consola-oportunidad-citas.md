$markdownContent = @"
# Consola Gestión Oportunidad de Citas y Consulta Externa (HOSVITAL HIS)

## 1. Ficha Técnica General

| Parámetro | Detalle Técnico / Institucional |
| :--- | :--- |
| **Nombre del Tablero** | Consola 16 - Oportunidad, Efectividad y Control de Inasistencias |
| **Plataforma de BI** | Apache IntelliHealth (Versión 6.1.0) |
| **Fuente de Datos / Motor** | Microsoft SQL Server (HOSVITAL HIS Database) |
| **Objeto Semántico Base** | Vista SQL: `VW_OPORTUNIDAD_CITAS_EXTERNA` |
| **Responsable de Arquitectura** | Presales & Healthcare Solutions Specialist (DigitalWare Suite) |
| **Público Objetivo** | Dirección Médica, Coordinadores de Citas y Jefes de Servicios Ambulatorios |

---

## 2. Propósito y Alcance

### 2.1 Propósito
La de Oportunidad de Citas y Consulta externa está diseñada para ofrecer visibilidad gerencial y control operativo en tiempo real sobre la gestión de citas de consulta externa en instituciones prestadoras de servicios de salud (IPS). Su objetivo central es medir con precisión la oportunidad de asignación (*lead time*), evaluar la efectividad en la asistencia de los pacientes, mitigar el ausentismo y garantizar el cumplimiento de los estándares normativos y contractuales con las entidades aseguradoras (EPS).

### 2.2 Alcance
* **Cobertura Temporal:** Análisis histórico y dinámico filtrado por rangos de fechas (desde gestión diaria hasta cortes anuales).
* **Cobertura Operativa:** Aplica a todas las sedes asistenciales conectadas al esquema multi-sede de HOSVITAL HIS.
* **Segmentación Analítica:** Desglose por especialidades médicas, aseguradores (EPS / contratos), estados clínicos de la cita (incluyendo cancelaciones bajo códigos 'N' y 'X') y centros de atención.

---

## 3. Modelo de Datos y Origen de Información

### 3.1 Tablas Involucradas en HOSVITAL HIS
La construcción de la vista semántica consolida la información transaccional proveniente de las siguientes tablas del núcleo de citas y admisiones de HOSVITAL:
* `CITMED` / `CITMED1`: Tablas transaccionales de agenda, programación y estados de citas.
* `MAEMED1` / `maeesp` / `maepro`: Catálogos maestros de profesionales, especialidades y procedimientos.
* `maeemp` / `empress`: Datos normativos de contratos y aseguradores.

### 3.2 DDL de la Vista Semántica Actualizada
```sql
ALTER VIEW [dbo].[VW_OPORTUNIDAD_CITAS_EXTERNA] AS
SELECT  
    c.CitNum AS Id_Cita,
    c.CitSed AS Codigo_Sede,
    c.CitFec AS Fecha_Cita,
    c1.CitFecPa AS Fecha_Requerida_Paciente,
    DATEDIFF(day, c1.CitFecPa, c.CitFec) AS Dias_Espera,
    c.CitCodMed AS Codigo_Medico,
    LTRIM(RTRIM(
        ISNULL(m.MNom1, '') + ' ' + 
        ISNULL(m.MNom2, '') + ' ' + 
        ISNULL(m.MApe1, '') + ' ' + 
        ISNULL(m.MApe2, '')
    )) AS Nombre_Medico,
    c.CitEspMed AS Codigo_Especialidad,
    ISNULL(e.MENomE, 'SIN ESPECIFICAR') AS Nombre_Especialidad,
    c.CitPro AS Codigo_Procedimiento,
    ISNULL(p.prnomb, 'SIN PROCEDIMIENTO') AS Descripcion_Procedimiento,
    c.CitPriVez AS Indicador_Primera_Vez,
    c1.citesta AS Estado_Cita_Codigo,
    CASE UPPER(LTRIM(RTRIM(c1.citesta)))
        WHEN 'F' THEN 'Facturada'
        WHEN 'C' THEN 'Confirmada'
        WHEN 'N' THEN 'Cancelada'
        WHEN 'X' THEN 'Cancelada'
        WHEN 'A' THEN 'Atendida'
        WHEN 'I' THEN 'Incumplida'
        WHEN 'R' THEN 'Reservada'
        WHEN 'L' THEN 'Con Multa Levantada'
        WHEN 'M' THEN 'Con Multa'
        ELSE ISNULL(c1.citesta, 'NO DEFINIDO')
    END AS Estado_Cita,
    c.CitTip AS Tipo_Cita_Codigo,
    CASE c.CitTip
        WHEN 'I' THEN 'Cita Individual'
        WHEN 'G' THEN 'Cita Grupal'
        WHEN 'j' THEN 'Junta Medica'
        ELSE 'OTRO'
    END AS Tipo_Cita,
    c.CitClas AS Clasificacion_Cita_Codigo,
    CASE c.CitClas
        WHEN 'CO' THEN 'Cita Corriente'
        WHEN 'PP' THEN 'Cita de PyP'
        WHEN 'PT' THEN 'Cita plan de tratamiento'
        ELSE 'OTRO'
    END AS Clasificacion_Cita,
    c1.CitNroCto AS Codigo_Contrato,
    ISNULL(emp.EmpDsc, 'SIN DESCRIPCION CONTRATO') AS Descripcion_Contrato,
    emp.MEcntr AS Nit_Asegurador,
    ISNULL(mae.MENOMB, 'SIN ASEGURADOR') AS Nombre_Asegurador
FROM dbo.CITMED c WITH (NOLOCK)
LEFT JOIN dbo.citmed1 c1 WITH (NOLOCK) 
    ON c.CitNum = c1.CitNum
LEFT JOIN dbo.maeemp mae WITH (NOLOCK) 
    ON RTRIM(c1.CitNroCto) = RTRIM(mae.mennit)
LEFT JOIN dbo.empress emp WITH (NOLOCK) 
    ON RTRIM(mae.MEcntr) = RTRIM(emp.MEcntr)
LEFT JOIN (
    SELECT MMCODM, 
           MAX(MNom1) AS MNom1, 
           MAX(MNom2) AS MNom2, 
           MAX(MApe1) AS MApe1, 
           MAX(MApe2) AS MApe2
    FROM dbo.MAEMED1 WITH (NOLOCK)
    GROUP BY MMCODM
) m ON c.CitCodMed = m.MMCODM
LEFT JOIN (
    SELECT MECodE, MAX(MENomE) AS MENomE
    FROM dbo.maeesp WITH (NOLOCK)
    GROUP BY MECodE
) e ON c.CitEspMed = e.MECodE
LEFT JOIN (
    SELECT prcodi, MAX(prnomb) AS prnomb
    FROM dbo.maepro WITH (NOLOCK)
    GROUP BY prcodi
) p ON RTRIM(c.CitPro) = RTRIM(p.prcodi);
```
## 4. Reglas y Lógica de Negocio
* Exclusión de Anulaciones: Las citas con estado 'X' (Anuladas) son eliminadas del universo de análisis para evitar sesgos en el cálculo de volumen y demanda real.

* Cálculo de Oportunidad: Los días de espera se calculan mediante la diferencia en días entre la fecha en que el paciente requiere la cita (CitFecPa) y la fecha asignada (CitFec), aplicando filtros de acotación para descartar valores atípicos.

* Control de Ceros: Las métricas de promedio incorporan funciones de manejo de nulos (ISNULL) para asegurar una renderización limpia en los componentes de IntelliHealth.

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

| Métrica | Expresión Lógica / SQL | Descripción de Negocio |
| :--- | :--- | :--- |
| **Promedio Días de Espera** | `ISNULL(AVG(CAST(Dias_Espera AS FLOAT)), 0)` | Lead time promedio transcurrido entre la solicitud y la asignación del recurso. |
| **Tasa de Asistencia Global** | `SUM(CASE WHEN Estado_Cita = 'Atendida' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0)` | Porcentaje de cumplimiento efectivo frente al total de citas programadas. |
| **Volumen de Demanda** | `COUNT(*)` | Cantidad total de citas gestionadas en la ventana de tiempo. |

## 6. Consultas SQL por cada Chart
* **1. KPI Promedio Días de Espera:**

```SQL
SELECT ISNULL(AVG(CAST(Dias_Espera AS FLOAT)), 0) AS metric 
FROM VW_OPORTUNIDAD_CITAS_EXTERNA 
WHERE Dias_Espera >= 0;
```
* **2. Gráfico Oportunidad por Especialidad:**

```SQL
SELECT Nombre_Especialidad, ROUND(AVG(CAST(Dias_Espera AS FLOAT)), 1) AS Promedio_Dias 
FROM VW_OPORTUNIDAD_CITAS_EXTERNA 
WHERE Dias_Espera > 0 
GROUP BY Nombre_Especialidad 
ORDER BY Promedio_Dias DESC;
```
* **3. Análisis de Demanda y Efectividad:**

```SQL
SELECT Nombre_Especialidad, COUNT(*) AS Volumen_Citas, 
       SUM(CASE WHEN Estado_Cita = 'Atendida' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Tasa_Efectividad 
FROM VW_OPORTUNIDAD_CITAS_EXTERNA 
GROUP BY Nombre_Especialidad;
```

* ** 4.Tasa de Asistencia Global (KPI)**
```SQL
SELECT 
    ISNULL(
        SUM(CASE WHEN Estado_Cita = 'Atendida' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), 
        0
    ) AS metric 
FROM VW_OPORTUNIDAD_CITAS_EXTERNA;
```
Cómo verificar: El valor devuelto debe coincidir con el porcentaje global de pacientes que asistieron efectivamente a su cita frente al total programado.

* ** 5. Distribución de Citas por Estado (Gráfico de Dona / Pie)** 

```SQL
SELECT 
    Estado_Cita, 
    COUNT(*) AS Total_Citas,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS Porcentaje
FROM VW_OPORTUNIDAD_CITAS_EXTERNA
GROUP BY Estado_Cita
ORDER BY Total_Citas DESC;
```

* **6. Volumen y Efectividad por Especialidad (Gráfico Combinado / Barras y Líneas)**

```SQL
SELECT 
    Nombre_Especialidad, 
    COUNT(*) AS Volumen_Citas,
    SUM(CASE WHEN Estado_Cita = 'Atendida' THEN 1 ELSE 0 END) AS Citas_Atendidas,
    ROUND(
        SUM(CASE WHEN Estado_Cita = 'Atendida' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), 
        2
    ) AS Tasa_Efectividad
FROM VW_OPORTUNIDAD_CITAS_EXTERNA
GROUP BY Nombre_Especialidad
ORDER BY Volumen_Citas DESC;
```
* **7. Citas por Asegurador y Estado (Gráfico de Barras Apiladas)**
```SQL
SELECT 
    Nombre_Asegurador, 
    Estado_Cita, 
    COUNT(*) AS Cantidad_Citas
FROM VW_OPORTUNIDAD_CITAS_EXTERNA
GROUP BY Nombre_Asegurador, Estado_Cita
ORDER BY Nombre_Asegurador, Cantidad_Citas DESC;
```
Cómo verificar: Al filtrar por un asegurador específico (EPS) en el tablero, las barras se desglosarán mostrando el volumen segmentado por cada estado clínico.

* **8. Promedio Días de Espera por Especialidad (Gráfico de Barras Horizontales)**
```SQL
SELECT 
    Nombre_Especialidad, 
    ISNULL(ROUND(AVG(CAST(Dias_Espera AS FLOAT)), 1), 0) AS Promedio_Dias 
FROM VW_OPORTUNIDAD_CITAS_EXTERNA 
WHERE Dias_Espera >= 0 
GROUP BY Nombre_Especialidad 
ORDER BY Promedio_Dias DESC;
```
Cómo verificar: Los valores numéricos en días deben mantenerse dentro de rangos operativos lógicos (por ejemplo, entre 0 y 45 días), sin picos causados por datos atípicos o negativos.

* **9. Detalle Operativo de Citas (Tabla Analítica / Listado)**

```SQL
SELECT 
    Id_Cita,
    Fecha_Requerida_Paciente,
    Fecha_Cita,
    Dias_Espera,
    Nombre_Sede,
    Nombre_Especialidad,
    Nombre_Asegurador,
    Estado_Cita
FROM VW_OPORTUNIDAD_CITAS_EXTERNA
ORDER BY Fecha_Cita DESC;
```
Cómo verificar: La tabla debe permitir la búsqueda rápida de registros individuales y mostrar orden cronológico inverso para auditoría de los coordinadores.

## 7. Estructura y Configuración del Dashboard (IntelliHealth 6.1.0)

### 7.1 Esquema de Distribución en Grilla
* **Franja Superior (KPIs Ejecutivos):** Tarjetas de número gigante para *Tasa de Asistencia Global* y *Promedio Días de Espera* equipadas con semáforos de alerta.
* **Franja Central (Análisis de Demanda y Oportunidad):** Gráfico de barras horizontales para el promedio de días por especialidad y gráfico combinado de volumen y efectividad.
* **Franja Inferior (Auditoría y Detalle):** Gráfico de distribución de citas por estado, desglose por asegurador y tabla analítica operativa.

### 7.2 Detalle de Configuración y Paleta Institucional

Configuración de umbrales en IntelliHealth:

* **Semáforo de Oportunidad (Días de Espera):** Óptimo `0 <= x <= 15` (Verde); Alerta `16 < x <= 30` (Amarillo); Crítico `x > 30` (Rojo).
* **Semáforo de Asistencia:** Crítico `< 70%`; Precaución `70% - 80%`; Óptimo `> 80%`.

```json
{
  "theme_colors": {
    "success": "#28a745",
    "warning": "#ffc107",
    "danger": "#dc3545",
    "primary": "#007bff"
  },
  "formatting_rules": {
    "oportunidad_optimal_range": "0 <= x <= 15"
  }
}
```