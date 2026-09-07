# PROGPYP11

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPPCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPPCodAct`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPPCtvEda`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPPAEdIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPAEdInE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPAEdFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPAEdFiE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
