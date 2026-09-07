# REIRESEN1

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
| 🔑 | **`REIREnCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRTipEn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResVal`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResSel`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREnPa1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
