# NIDESFINP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIHOPNO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTCOD`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIHOPDDI`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIHOPDDF`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIHOPDTZ`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIHOPDVP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIHOPDVE`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
