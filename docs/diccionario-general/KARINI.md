# KARINI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovUbiEst`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovUbiDIz`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovUbiNiv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovUbiZon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MovUbiCan`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
