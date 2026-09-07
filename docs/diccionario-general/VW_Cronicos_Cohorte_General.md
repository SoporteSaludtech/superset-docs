# VW_Cronicos_Cohorte_General

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`Identificacion`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Nombre_Paciente`** | `char(243)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Entidad_Contrato`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Codigo_CIE10`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Cohorte`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Presion_Sistolica`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Presion_Diastolica`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Hora_Tension`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Cod_Cup_Lab`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Resultado_Laboratorio`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ingreso_HC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ATENCION`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`Telefono`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tiene_Ingreso_Posterior`** | `int` | NO | Campo transaccional de Hosvital HIS |
