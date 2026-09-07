# RIASEDAD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACodAct`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACtvEda`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAAEdini`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAAEdInE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAAEdFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAAEdFiE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
