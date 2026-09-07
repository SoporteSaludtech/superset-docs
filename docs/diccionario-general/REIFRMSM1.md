# REIFRMSM1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REISumCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REISumEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFhHrAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndRnl`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REImInCAd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuApl`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuSus`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecPAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICtvIn1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObApMd`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICanSuD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISumDev`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICnsEsA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFrm1Pa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
