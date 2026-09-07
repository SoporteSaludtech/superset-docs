# FRMSMNS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSumCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCSumEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFhHrAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIndRnl`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASmIndCAd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASUsuApl`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASUsuSus`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASFecPApl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HICtvIn1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASObApMd`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCanSuD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSumDev`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCnsEsA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESODES`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCSumFPT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
