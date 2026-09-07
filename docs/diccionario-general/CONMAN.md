# CONMAN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConManCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConManMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManAni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
