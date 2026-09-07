# REIFRMSMH

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
| 🔑 | **`RMSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RMSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RMSPrac`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RCncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRSmCnD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
