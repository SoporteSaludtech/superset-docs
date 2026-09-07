# REPATSDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RATAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RATMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RATCsc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RATTipInf`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATCodSus`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTipIde`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATIde`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTipCmp`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATParRel`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTip`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRazSoc`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATEst`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPunEmi`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATSec`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFecEmi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATAut`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBNGIva`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBasImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBImGra`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBImExe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATICE`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATIVA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI10`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI20`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI30`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI50`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI70`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRI100`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRINDev`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPagRes`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTipReg`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPRePRG`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPRePPF`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATDenRFP`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPaiPag`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATConDTP`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATSujRNL`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPRFPre`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATForPag`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATCRFIRe`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBImRen`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPRFIRe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATMonRRe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFchPDi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATImpReS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATAUtDiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATEstRet`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPunRet`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATSecRet`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATAutRet`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFECRet`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATDocMod`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATEstMod`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPunMod`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATSecMod`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATAutMod`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATCTCRee`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTIPRee`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATNIPRee`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATEstRee`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATPunRee`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATSecRee`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFchRee`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATAutRee`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBImRee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBIGRee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBINRee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATBIERee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTBIRee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATICERee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATIvaRee`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTipEmi`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATNumCom`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTipCom`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATCom`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATIvaRet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATRenRet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATVen`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATIvaCom`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
