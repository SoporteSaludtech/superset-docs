# HCCOM1

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
|  | **`HISCCIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`hiscfk`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPNroEmb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPEddMat`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPEddPat`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPIndCEm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPPesNac`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPApg1Mn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPApg5Mn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPApg10M`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPIndVCm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnPDscDPs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCFCON`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCHORA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCMMED`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCLPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndCaC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndLiA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndCaP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndHxQ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDHQxSit`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndBaC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCdIndTdT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndOst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndEsc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndOtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDIndOtC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCDOtrObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FHCIndEsp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCFAC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCENFACT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESTEMB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISValAlc`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscPlm`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscOcu`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscGst`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscEnd`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscLcm`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RxSDscSNP`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EFsDscPlm`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HccauExt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFinCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCDIASIN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTCONDUS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCDISCA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCGRADO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFING`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFSAL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCLTR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCnCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FHCCodCto`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FHCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCtvIn1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFHorAt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolOri`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolEOr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolPPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolPPe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisIndApB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisIndFol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisIndEmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGCtv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisOriSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolAmb`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCitNum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisTrgReg`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisImgOdo`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisMotCie`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCULTCONS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPUEPRO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRESHEM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCONCOD`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFECSAL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODPAB`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTIPCAU`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCINDSOTR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISUSUDSD`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODESPE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODMEDES`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisOrient`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisIndPart`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFCIEFO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOrSeCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIdGenCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGEnCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NroPrescMIPRES`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisOrMov`** | `nchar(20)` | SI | Campo transaccional de Hosvital HIS |
