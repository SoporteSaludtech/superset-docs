# REIINTER

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
| 🔑 | **`MECodE`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIIntEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIFchRs`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObsOrd`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIDscRs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIUsrRs`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINumAue`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIReqAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINroAtu`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICtvEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsrCan`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFchCan`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIOrAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAuto`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDiaPT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIICauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICitAsi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
