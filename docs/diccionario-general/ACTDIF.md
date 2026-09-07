# ACTDIF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcDCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcDDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GActDCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTiAmor`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGActDCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDEstR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDDocRe`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDVlrBas`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMPCOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDPorImp`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDVlrIm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDVlrTot`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDVlrCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDFchCo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActUti`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActSubUti`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActCto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActSubCto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDFoDis`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCCdg`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDDscLa`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDCosHis`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDAmNor`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDModAj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDIndAj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDMetAm`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDAjCt0`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDAjuAm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUltAj`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUltAm`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDSdoAm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDNoMov`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDFeCr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUsuCr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDfeMd`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUsuMd`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUltPaa`** | `decimal(7,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDNrA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUltAni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDUltMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDPorAju`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActDPorDep`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActTipAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDNroEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDDocEnt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDCscEnt`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDFchEnt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTOpTb`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
