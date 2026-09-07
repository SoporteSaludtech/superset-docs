# INGRESOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IngFecAdm`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNit`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEntDx`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngHsp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngExtEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEstSld`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUsrReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIPS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFecEgr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSalDx`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNotObl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEntDx2`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNmResp`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNmResp2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDocResp`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTDoResp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngParResp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDirResp`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTelResp`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InsIpsSal`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFchM`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCauM`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMedSal`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMEdEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMedDef`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InCerDef`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxSal1`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxTip1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxSal2`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxTip2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxSal3`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngComp`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMotSal`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngHorObs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUsrSal`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCodP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNumC`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDoAco`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNoAc`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTeAc`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTeTrR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEmTrR`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDptRe`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMunRe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCoMt`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEsMt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngApRes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngApRes2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCtvAc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxCli`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngInSlC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodPEg`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngAteEgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNumCit`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCscN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSege`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCoPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTiPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTiAn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngQuiA`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUCtvEp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodCEg`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngObsAnu`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDerObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngAtnAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUlcMoP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngReaUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEmpPlt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSedPlt`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodPlt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCnsPlt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngResExe`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngHosTTo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFeHAtU`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndApB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIPSAtn`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNroAn1`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNroAn2`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProTerCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngReligi`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngAcudie`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDesAlm`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndUF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngActAla`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngObsAla`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSoAdTr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMeSAT`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEsSAT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFSAdTr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndReN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndAte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngEsDepo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNumTur`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFecTur`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngRieCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngRiCnDe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngRiCoDe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDxRie`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGCODPAQ`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngAteEs`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngGruPo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCarnet`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGSALML`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGDXSAL4`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGDXTIP3`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngParAc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTiDoAc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGDEPPLA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGREIPAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodEnt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngIndCamT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGCODCON`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGFEPRCON`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngRfrSld`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngExCpPF`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngParDetO`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngNumTel`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngInsEnt`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFueInf`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngTipLle`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngObsSal`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngConSal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INGMAIRES`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodMAte`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngPeSoAl`** | `nvarchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngVia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSalEnf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngSalEnE`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
