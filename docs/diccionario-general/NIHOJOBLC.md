# NIHOJOBLC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIHOJNO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTCOD`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIHOJCF`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIHOJCU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIHOJCO`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIHOJCE`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
