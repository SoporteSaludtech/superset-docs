# HCCOM51

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
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCPrcTpoP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrcEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFcHrOrd`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFcHrAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCResult`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPrUsrRgs`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCConclu`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCtvIn51`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIntRes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFeHInt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFolInt`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMedInt`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrEsFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrcHrRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCNumAuE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSedPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCodFor`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVerFor`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCnsFac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIngFacC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFecReI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFecProI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCNumDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCarDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCObsCan`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrUsCaD`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrFhCaD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAteAgOd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFcHrPro`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCProCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDisTri`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEstDis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMedDis`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOrdAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUrlIma`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFOLATN`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMoCnTp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODESP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODMED`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCORDRES`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVOLORD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCREQTRA`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPROPER`** | `nchar(18)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRECMUE`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDOSRDTP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrRUCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCnlCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCnlTpo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFOLOP`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
