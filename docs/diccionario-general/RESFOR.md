# RESFOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`codResol`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESFORSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESPRESEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESSEGSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESFORCOL`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESFORORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESFOREST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESFORNUM`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
