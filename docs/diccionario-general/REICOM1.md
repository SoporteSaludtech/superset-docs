# REICOM1

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
|  | **`REICCIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIcfk`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPNroEmb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPEdMat`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPEdPat`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPIndCEm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPesNac`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPApg1Mn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPApg5Mn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPApg10M`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPInVCm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDscDps`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICFCON`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICHora`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICLPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndCac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndLiA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHQxSit`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndBac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndTdt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndOst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndEsc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndOtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIndOtc`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndEsp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICFAC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICENFACT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIESTEMB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDPl`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDOc`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDGs`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDEn`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDLc`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRxSDSNP`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIExFDPl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIcauExt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDiaSin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConUsu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDISCA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIGRADO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFING`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFSAL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICLTR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCnCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodCto`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REItvIn1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFHorAt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolOri`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolEOr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIULTCON`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolPPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolPPe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFinCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndApB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndFol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndEmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIOriSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolAmb`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHCitNu`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIGCtv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITrgReg`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIValAlc`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIImgOdo`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMotCie`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREIPa1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICDOtOb`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
