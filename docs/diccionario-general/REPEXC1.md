# REPEXC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepClCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RepDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepCons`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepOriCon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepDetCon`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepFor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepXLS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepVis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepGra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepCSV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepDQY`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
