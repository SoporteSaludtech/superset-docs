# HCRIASUMI

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
| 🔑 | **`HRIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIAMsCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIAMsPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIAMsForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIACncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIASuCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HRIASuTrDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASuFEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASuSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASuTAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRRIASuEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASUAsFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASUOrFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASUApFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRIASuFOr`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRIASuFAp`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASEsAsg`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASEsOrd`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASEsApl`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASAtAsg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASAtOrd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIASAtApl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
