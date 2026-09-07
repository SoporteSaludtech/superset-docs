# SOCAFIEM2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`SOcCSec`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcCKey`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcEmpCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcCarCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcAEnAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcAEnMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcAEnTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SOcAEnPAf`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcAEnNat`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcAEnDIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcAEnSec`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMCodi`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOObsEAA`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
