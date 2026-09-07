# FRMESQDEF

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
| 🔑 | **`FrmDefCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FrmDefDos`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrmDefCad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrmDefTCa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrmDefPor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrmDefTPo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FRMDEFNAP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMDEFUDD`** | `money` | SI | Campo transaccional de Hosvital HIS |
