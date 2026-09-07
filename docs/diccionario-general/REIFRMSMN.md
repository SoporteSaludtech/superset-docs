# REIFRMSMN

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
|  | **`REIOBSFOR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFhrReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICanSum`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUndCd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFSVia`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFSFrH`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISmCnDs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrReCd`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIStGr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMtpCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUseDsp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFcHrDs`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISmAuNr`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISmAuNo`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndCDA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDscMdc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntDia`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHorIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITiTrDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDiaTra`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInDos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsNDsp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFhNDsp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICauNDs`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMedPac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFHorOr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntDsf`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUmdDsf`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolOrg`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFCtvEn`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFiTrAdi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFCscCoC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEsqCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndEsq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsrEsq`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIForPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuAcF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeHAcF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuDeF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeHDeF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIdTipI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstFoP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInEnFP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoOrFP`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsrEnf`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeHEnf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFMSRES`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINroEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFEntDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITipSum`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFApUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFApFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFApMtv`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFApIPS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMSRESH`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFAuto`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINroEnA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntEnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFFcDeP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFCntND`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFCscCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISSusRe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEmCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMCpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICscFrm`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDosUnK`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMedMaG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntSol`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHCF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFSFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
