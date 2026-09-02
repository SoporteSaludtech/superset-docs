# Consola y Estadísticas de Trauma

## 📌 Contexto y Objetivo
El **Dashboard de Consola y Estadísticas de Trauma** es una herramienta analítica y operativa desplegada en Apache Superset. Su objetivo principal es permitir la visualización, auditoría y análisis detallado de los pacientes ingresados por causas externas asociadas a trauma en la base de datos `HOSVITAL HIS`. 

El tablero no posee filtros de fecha "hardcodeados" en las vistas, delegando el control temporal al filtro nativo global del dashboard.

---

## 🗄️ Datasets Utilizados (SQL Server)

| Dataset en Superset | Tipo | Propósito | Columna Temporal |
|---------------------|------|-----------|------------------|
| `VW_Trauma_Consolidado` | Vista | Totales agrupados por servicio y diagnóstico. | `FECHA_ATENCION` |
| `VW_Trauma_Universo_Pacientes`| Vista | Detalle clínico y administrativo (Consola). | `FECHA_ATENCION` |
| `VW_Trauma_Prevalencia_Demografia` | Vista | Estratificación quinquenal y de género. | `FECHA_ATENCION` |
| `VW_Trauma_Auditoria_Causas` | Vista | Calidad de codificación de causas externas. | `FECHA_ATENCION` |

---

## 📊 Componentes Visuales (Charts)

## 1. Arquitectura de Datos (SQL Server)
A continuación se detallan las estructuras T-SQL implementadas en el motor de base de datos para alimentar los datasets del dashboard. Todas las vistas exponen el campo `FECHA_ATENCION` para la correcta homologación del filtro temporal.

### 1.1 Vista: Universo Operativo de Pacientes
Provee el detalle transaccional. Es la base para la consola operativa.
```sql
CREATE VIEW [dbo].[VW_Trauma_Universo_Pacientes] AS
SELECT 
    P.Identificacion,
    P.Nombre_Paciente,
    P.Sexo,
    dbo.FN_Calcular_Quinquenio(P.Fecha_Nacimiento) AS Grupo_Quinquenal,
    A.Pabellon,
    C.Nombre_Contrato,
    D.Codigo_CIE10,
    D.Descripcion_Diagnostico,
    A.Causa_Externa,
    A.FECHA_ATENCION
FROM Pacientes P
INNER JOIN Atenciones A ON P.Id_Paciente = A.Id_Paciente
INNER JOIN Contratos C ON A.Id_Contrato = C.Id_Contrato
INNER JOIN Diagnosticos D ON A.Id_Diagnostico = D.Id_Diagnostico
WHERE A.Causa_Externa LIKE '%Trauma%' OR A.Causa_Externa IN ('W00-X59', 'V01-V99');
```
### 1.2 Vista: Consolidado por Servicio y Diagnóstico
Pre-agrega dimensiones descriptivas para el cálculo de pacientes únicos.

```SQL
CREATE VIEW [dbo].[VW_Trauma_Consolidado] AS
SELECT 
    A.Id_Paciente,
    A.Pabellon AS Pabellon_Servicio,
    A.Causa_Externa,
    D.Codigo_CIE10 AS CIE10,
    D.Descripcion_Diagnostico,
    A.FECHA_ATENCION
FROM Atenciones A
INNER JOIN Diagnosticos D ON A.Id_Diagnostico = D.Id_Diagnostico
WHERE A.Ind_Trauma = 1;
```

### 1.3 Vista: Prevalencia Demográfica
Estructura optimizada para el conteo de frecuencias por edad y sexo.

```SQL
CREATE VIEW [dbo].[VW_Trauma_Prevalencia_Demografia] AS
SELECT 
    P.Id_Paciente,
    dbo.FN_Calcular_Quinquenio(P.Fecha_Nacimiento) AS Grupo_Quinquenal,
    P.Sexo,
    1 AS Tiene_Trauma,
    A.FECHA_ATENCION
FROM Pacientes P
INNER JOIN Atenciones A ON P.Id_Paciente = A.Id_Paciente
WHERE A.Ind_Trauma = 1;
```

### 1.4 Vista: Auditoría de Causas Externas
Clasifica la calidad del registro clínico para indicadores de gestión.

```SQL
CREATE VIEW [dbo].[VW_Trauma_Auditoria_Causas] AS
SELECT 
    A.Id_Atencion,
    CASE 
        WHEN A.Causa_Externa IS NOT NULL AND D.Codigo_CIE10 LIKE 'S%' THEN 'TR' 
        ELSE 'Incorrecto' 
    END AS Estado_Calidad,
    A.FECHA_ATENCION
FROM Atenciones A
INNER JOIN Diagnosticos D ON A.Id_Diagnostico = D.Id_Diagnostico;
```

### 1. Distribución de Trauma por Quinquenio y Género
* **Tipo:** Bar Chart (Barras agrupadas verticales)
* **Dataset:** `VW_Trauma_Prevalencia_Demografia`
* **Métrica:** `SUM(Tiene_Trauma)` (Pacientes con Trauma)
* **Dimensiones (Eje X / Desglose):** `Grupo_Quinquenal` / `Sexo`
* **Descripción:** Permite visualizar el volumen de pacientes estratificados por edad y género para identificar prevalencias demográficas.

### 2. Auditoría de Calidad - Causas Externas
* **Tipo:** Pie Chart (Formato Dona, Inner Radius 50%)
* **Dataset:** `VW_Trauma_Auditoria_Causas`
* **Métrica:** `COUNT(*)` (Total de Registros)
* **Agrupación:** `Estado_Calidad`
* **Descripción:** Gráfico ejecutivo que audita la proporción de registros correctos (TR) frente a codificaciones erróneas.

### 3. Consolidado de Trauma por Servicio y Diagnóstico
* **Tipo:** Table (Modo Aggregate)
* **Dataset:** `VW_Trauma_Consolidado`
* **Métrica:** `COUNT_DISTINCT(Id_Paciente)` (Pacientes Únicos)
* **Columnas de Agrupación:** `Pabellon_Servicio`, `Causa_Externa`, `CIE10`, `Descripcion_Diagnostico`
* **Descripción:** Resumen estadístico habilitado con paginación y búsqueda libre.

### 4. Universo Operativo de Pacientes con Trauma
* **Tipo:** Table (Modo Raw Records)
* **Dataset:** `VW_Trauma_Universo_Pacientes`
* **Columnas:** `Identificacion`, `Nombre_Paciente`, `Sexo`, `Grupo_Quinquenal`, `Pabellon`, `Nombre_Contrato`, `Codigo_CIE10`, `Descripcion_Diagnostico`, `Causa_Externa`, `FECHA_ATENCION`
* **Descripción:** Consola transaccional detallada para control operativo, búsqueda y exportación de registros.

---

## ⚙️ Configuración de Filtros
El dashboard está gobernado por un componente **Time Range Filter** global:
* **Nombre:** Periodo de Análisis
* **Scoping:** Todo el dashboard (All panels).
* **Mapeo:** Vinculado internamente a la columna `FECHA_ATENCION` en la sección *Filters* de cada uno de los 4 charts.
