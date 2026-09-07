# REIRESENC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIRDocPa`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIRTDoPa`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIRFolPa`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIRCtvRe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRFecHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIReDxAs`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREmPyP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRSePyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRPrPyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRAcPyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRePrCn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRePrCo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIReDoCo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREnPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRsFOHc`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMsCodi`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMsPrAc`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMsForm`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICncCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
