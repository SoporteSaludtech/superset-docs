# FRMSMNSAP

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
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCSUMCNSAP`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCSUMFECAP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMESTAP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMCNTAP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMFOLOR`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMOBSAP`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMCLPR`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMDIAA`** | `nchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMESDSP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMDOCDE`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMCNTDO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMCNTUD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMFECUA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMUSUAP`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMNOVAP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSUMNOVOB`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESODEA`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
