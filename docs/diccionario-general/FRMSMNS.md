# FRMSMNS

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
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FSmFhrReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCOBSFOR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`hisCanSum`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmUndCd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFSVia`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFSFrH`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmCnDsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrsRecCd`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmStGr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMtpCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUserDsp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFcHrDsp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmAutNro`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSmAutNom`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSmIndCDA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HICtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmDscMdc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSmCntDia`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsIndEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsHorIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrmSmUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsTiTrDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDiaTra`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmInDos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmUsNDsp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFhNDsp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCauNDs`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmMedPac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFHorOr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFolOrg`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCtvEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsDiTrAdi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSCscCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EsqCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmIndEsq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmUsrEsq`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmForPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmUsuAcF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFeHAcF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmUsuDeF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFeHDeF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmIndTipI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmEstFoP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmInEnFP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFoOrFP`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmSPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmUsrEnf`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFeHEnf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmMSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmNroEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCntEnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmNroEnA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmEntDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmTipSum`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFApUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFApFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFApMtv`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFApIPS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmMSRESH`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmAuto`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmIndAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFchDeP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCntNDs`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSCscCopC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmSSusRe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmMCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCscFrm`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmDosUnK`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmMedMaG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmCntSol`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSmCntDsf`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSmUmdDsf`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFapEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFapSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFapDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmFapCtv`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMFEHPRA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMINFECH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMINUSER`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMINPRES`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMSUMITR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMUSUITR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`FRMCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFSORIFR`** | `nchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMDA`** | `nvarchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMDP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMDC`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMDR`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMFT`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMFM`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMFC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMCD`** | `nvarchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMOB`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTSMES`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFSORIKY`** | `nvarchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMINDPOS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTOSUL`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMVIAPLI`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMCNTOSM`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMCLRTOT`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMVLMTOT`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMPASREN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMVELINF`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMAPLFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMAPLUSU`** | `nchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMAPLFAC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMAPLOBS`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRRAPLMED`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTPRCI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FRMMOTSUS`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMSUMACT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMSUMACO`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMTOTDIS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMDEFNAP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMDEFUMC`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMDEFUDD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsmSPPCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMOBSCOP`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMUSUCOP`** | `varchar(11)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMINDCOP`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FsCscFrms`** | `numeric(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSUsrReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSFRANTUS`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSOBFRANT`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMCONUSR`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FSMFRANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
