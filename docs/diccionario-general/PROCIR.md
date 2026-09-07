# PROCIR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProEPS`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProVivo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProSit`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProDxppal`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProEsta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProOBs1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProTpAnst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProHSep`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFSep`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPersCnf`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PfcHrCnf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PUsrConf`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProMtCnTp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFliSol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFliCx`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProPerSep`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProEspSep`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProRValAn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProDurMn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProDurHr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProVia`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProLat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProResCam`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProTipCam`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProObRCam`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProReqHD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCodHD`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProObsHD`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCntHD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProDispEE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProObsEE`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProReMaE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProObMaE`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProPerSe1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProEspSe1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFecF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProHorI`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProHorF`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCons`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCirAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProObsT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCitNum`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCitEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProIndOpu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProRegOpe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProSedQr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProFecSR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProDxSali`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCompli`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PosTpHerd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PosCntSng`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxTmpPrf`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxTmpClm`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxIndVia`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PosDescri`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxHrIn`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxHrFn`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProMotCan`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PFcHrCnc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPersCnc`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPerCan`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ProIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProUsuUso`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProIndRei`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INSCODI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROONCESQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROPRTCOD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROORIGEN`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROPRCESQ`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROCANORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROVOLORD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROCODHEM`** | `nchar(18)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROINSCIR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROHEMCIR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCauCan`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCnlCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCnlTpo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONOTA`** | `varchar(3000)` | SI | Campo transaccional de Hosvital HIS |
