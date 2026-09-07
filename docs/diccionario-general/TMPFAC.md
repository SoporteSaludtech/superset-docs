# TMPFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFMENi`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFchI`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFFCES`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFHorI`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFDi1I`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDi2I`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDi1S`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDi3I`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MICodI`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SONume`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SONitAsg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOFchVIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOVePl`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOVeMa`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOVeTi`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOVeMo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOVeCl`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCndAcc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOSitAcc`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOFchAcc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCodD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCodM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SORulUrb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOInfAcc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOIndAsg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOFchVFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOTpICnd`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCedCnd`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SONomCnd`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SODirCnd`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SoCodDCnd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCodMCnd`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SoTelCnd`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SONomEmp`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOMCodFCD`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOMNroReg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SONomSuc`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOTpoEC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SODesEC`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCodDE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOCodME`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOInfEC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SODecla`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOTiDoDc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SODocDcl`** | `char(11)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOlugExp`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SoLgExpCn`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCCCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFViaI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoMI`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEsMI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEsMS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFEsH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNoRe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNoRe2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTeRe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTiRe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCMEg`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEstS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDi2S`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDi3S`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFMotS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCMAD`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSeGe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTiPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTiAn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFchM`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCaMu`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFQuia`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDiCp`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFHorO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFchS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVNPU`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUIng`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUSal`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNMAU`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFcNomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFcCodCam`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFcCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUscP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNrCerD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SccEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFUlcAC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEstP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotF`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFValS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVaAb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVAPU`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVPaU`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVDsc`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUscS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUcsA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUcsN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTpeAut`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrAut`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCpgPgo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCpgLqd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFcCodCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrImpt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFIndCrt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCnTQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReFatMat`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReFatNum`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmEdoCue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmCtvAct`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDocRep`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTDoRep`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDirRep`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFIPSENT`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDocAco`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNoAc`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTeAc`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTeTrRe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEmTrRe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDptRes`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFMunRes`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoMt`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEsMt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFApeRes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFApeRes2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ClaproI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoCamI`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFObsFac`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAdmFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUsuFac`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVPOCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrTIv`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCONCAP`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCODPAQ`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFDI4S`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFParAc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTiDocAc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNUMPGP`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFPoPla`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFParDetO`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFMAIRES`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
