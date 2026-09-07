# PARMINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParmCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParmDsc`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSInv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDTInv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDEInv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDBlta`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDLsP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmTRea`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTSCon`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTSAsi`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTDevA`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSRea`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDAut`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDPaq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSalDis`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDRqI`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDAjt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDSEnt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDSSal`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDSTra`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmTSCg`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmTDCg`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmTVDr`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFrmMI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmMetTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDEEsp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCalSto`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmSCPrv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmInFiLo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmModCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmAIF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDEInA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSInvA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDTInvA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmMAR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDoAcC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDCtvUb`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmNroCnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCxAn`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCxGl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocRC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocGlo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDReCj`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCFSR`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCFRd`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCNot`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmNFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNCCon`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDoFaPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDoOsPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNDeNCr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDOrdSrv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDTes`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCCar`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDCar`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNDFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocCFR`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMCEVPOR`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMPEVMES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMPEVTIP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParNcFaPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmAnfPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCoBar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCoSi`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDSalin`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDEnPrT`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDTrPr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSalins`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmEnPrT`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmTrPr`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCoBarP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmEACoB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmPrPla`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmNAPPl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmNCPPl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmRGPPl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`parNAnuFc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmGAnuC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
