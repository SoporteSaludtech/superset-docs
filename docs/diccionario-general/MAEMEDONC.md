# MAEMEDONC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAEMEDCSC`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAELINPRO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAERGPROD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEESTPRO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAETIPEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEESTCOM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAETIPCOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEVOLREC`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEUNDMER`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAECNCFIN`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEUNDMEF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEOBSGEN`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
