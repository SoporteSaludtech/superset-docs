# Consola Análisis de Ingresos

## Propósito Funcional
La **Consola Análisis de Ingresos** proporciona una visión operativa y analítica en tiempo real sobre el flujo de admisión de pacientes en la institución prestadora de salud. Permite auditar el volumen de demanda asistencial, discriminar la concentración entre admisiones ambulatorias frente a hospitalarias, identificar las especialidades tratantes con mayor carga y monitorear la demanda segmentada por entidades aseguradoras y convenios (EPS).

---

## Ficha Técnica del Tablero

| Atributo | Especificación |
| :--- | :--- |
| **Dominio Funcional** | Gestión Asistencial / Admisiones y Censo |
| **Periodicidad de Actualización** | 15 Minutos (Autorefresh IntelliHealth) |
| **Fuente de Datos** | SQL Server - Hosvital HIS (`WITH (NOLOCK)`) |
| **Tablas Transaccionales Core** | `CAPMMAE` (Maestro Pacientes), `ADINGRE` (Ingresos/Admisiones), `MAEESP` (Especialidades), `MAEEMP` (Aseguradores/EPS) |
| **Ecosistema Visual** | (Modo Oscuro Institucional) |

---

## Estructura de Filtros Globales

El tablero implementa una barra superior de filtros interactivos cruzados (*Cross-filtering*):

* **Rango Temporal (`Fecha desde`):** Permite acotar el análisis por periodos operativos (Día en curso, Semana epidemiológica, Mes o Rango personalizado sobre la fecha de admisión institucional).
* **Tipo de Atención:** Segmentador univaluado/multivaluado (`Ambulatorio`, `Hospitalización`).
* **Especialidad Tratante:** Selector paramétrico de especialidades activas para auditar la demanda médica puntual.

---

## Componentes Analíticos y Métricas

### 1. KPI – Total de Ingresos (Big Number)
* **Descripción:** Volumen neto de admisiones registradas en el periodo seleccionado bajo los criterios de filtro aplicados.
* **Fórmula SQL:**
  ```sql
  COUNT(DISTINCT ING.CONSECUTIVO_INGRESO);
 ```
 
 Uso Clínico: Monitoreo del volumen global de pacientes que ingresan al circuito de atención.

## 2. Distribución por Tipo de Atención (Donut Chart)
* **Descripción:** Proporción relativa de pacientes ingresados por canal ambulatorio versus pacientes que requieren cama hospitalaria.

* **Dimensiones:** Tipo_Atencion (Ambulatorio, Hospitalización).

* **Métrica:** COUNT(CONSECUTIVO_INGRESO).

Utilidad: Evaluación rápida del requerimiento de asignación de camas frente a demanda de consulta o procedimientos externos.

## 3. Top 10 Especialidades Médicas (Horizontal Bar Chart)
* **Descripción:** Clasificación descendente de los servicios médicos que reciben mayor asignación de pacientes al ingreso.

* **Dimensiones:** Especialidad_Tratante (Ej. Apoyo Diagnóstico, Cardiología, Cirugía Vascular, Urología, Ortopedia, UCI, Medicina General).

* **Métrica:** Conteo neto de admisiones por código de servicio tratante.

Utilidad: Dimensionamiento de personal médico asistencial y redistribución de turnos según demanda.

## 4. Top 10 Aseguradores y Convenios - EPS (Bar Chart)
* **Descripción:** Concentración del volumen de pacientes según su pagador o administradora de planes de beneficios (EAPB / EPS).

* **Dimensiones:** Razon_Social_EPS / Convenio.

* **Métrica:** COUNT(CONSECUTIVO_INGRESO).

Utilidad: Auditoría de concentración de cartera asistencial, pertinencia contractual y planeación financiera de servicios.

## 5. Auditoría Nominal: Ingresos Analizados (Interactive Table)
Descripción: Cuadro de detalle nominal fila por fila para auditoría y validación operativa.

Columnas Visibles:

* **FECHA_INGRESO:** Marca de tiempo exacta del ingreso asistencial.

* **FECHA_EGRESO:** Marca de tiempo de egreso o alta médica (si aplica).

* **NUMERO_IDENTIFICACION:** Documento de identidad del usuario.

* **TIPO_IDENTIFICACION:** Tipo documental (CC, TI, RC, etc.).

* **CONSECUTIVO_INGRESO:** Número de admisión único institucional.

* **NOMBRE_PACIENTE:** Nombres y apellidos completos.

* **TIPO_ATENCION:** Modalidad de servicio asignada.

* **CON_EGRESO:** Estado de alta asistencial (Si / No).

* **SERVICIO_INGRESO:** Pabellón o área física de recepción (Ej. Hospitalización General).

* **NUMERO_CAMA:** Identificador físico de la cama asignada (en admisiones intrahospitalarias).

Estándares de Visualización y Rendimiento
Desactivación de Cell Bars:

En la tabla Ingresos Analizados, la opción Show Cell Bars debe mantenerse desmarcada (☐) en la pestaña Customize para evitar fondos verdes artificiales sobre el consecutivo de ingreso y preservar la legibilidad en modo oscuro.

Lectura no bloqueante:

La vista que alimenta el dataset debe incluir la cláusula de aislamiento para evitar contención de bloqueos transaccionales:

 ```SQL
FROM dbo.ADINGRE AS ING WITH (NOLOCK)
INNER JOIN dbo.CAPMMAE AS PAC WITH (NOLOCK) 
    ON ING.HISTORIA = PAC.HISTORIA;
 ```
 