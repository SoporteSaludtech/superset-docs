# FRMSMNSAL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSUMCNSAP`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSUMSRES`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSUMPRVC`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSUMLOTC`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMFECV`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCSUMCNTAL`** | `money` | NO | Campo transaccional de Hosvital HIS |
