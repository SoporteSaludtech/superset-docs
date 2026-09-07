# FRMSMHU

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
| 🔑 | **`MMSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMSPrac`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MHCSmCnDsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MHCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FSHVOLPRG`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSHCNTCAL`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSHCNTVOL`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSHUNDMED`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSHREQDIA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSHCODCTR`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSCODPRO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
