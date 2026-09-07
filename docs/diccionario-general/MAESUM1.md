# MAESUM1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSNomG`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodBar`** | `char(14)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSPPub`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCodi`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSPrAc`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CncCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSForm`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mshomo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsTipo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsMatOst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUndCom`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSStMin`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSStMax`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMPCOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtaE1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtDE1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtaE2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtDe2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtDs1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtaI1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCtaS2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtDS2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsActFij`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsInvNeg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFchUlE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFchUlS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFctCnvC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsEstado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFctCCsm`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSSldUni`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSSldVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVlU1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovFchCom`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCstprm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsConPrm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSValU`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFchCr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUsuCr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSFchMd`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUsuMd`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsPPVU`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsGrpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsSGrpCd`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsConCos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsBasCos`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsMetCos`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsConMar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsBasMar`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsMetMar`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsConCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsMetCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsBasCon`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUndMct`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCncUnM`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCncCnt`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUndDes`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFactur`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCntRUso`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsTipReu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCtrlLot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CondCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsTpoRep`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SumIndVal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SumCntEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SumCntGrl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSMinDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSMaxDia`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUndApl`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsDUnsApl`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFrUndApl`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUndFct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsIndEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MarCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSAdmAdi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSDspAdi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsIndRem`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsActDif`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsRegInv`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFraUni`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsSValUni`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCodCUM`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsAltCos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsProGen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsMedReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSDiaEyEF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSIndMG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSClaDM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCSTPRMN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsImpGe`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSDispImp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSABLNPT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSPESGRA`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCLANPT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUMdCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFacDen`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFacOsm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFacVol`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsFacCal`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsApNuPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSINDPT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAES_ID`** | `varchar(36)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSMnjQR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`periodoVidaUtil`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`vidaUtil`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`codPresentComercial`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsCodTMed`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsDesTMed`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSImpSal`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCtaDFVD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSClaRDIV`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSActFRP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsAneste`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
