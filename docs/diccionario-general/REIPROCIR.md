# REIPROCIR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REIEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrCiCo`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrHorI`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrHorF`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrCons`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrEsta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrOBs1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrDxSa`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrComp`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPoTpHe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPoCnSn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDQxTmP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDQxTmC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDQxInV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPosDes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDQxHrI`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDQxHrF`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrTpAn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrMoCa`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrMtCT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPFcHrC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProEPS`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProSit`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProViv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrDxPp`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrPeSe`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrFSep`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrHSep`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPUsCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPfHrCn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPerCn`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrCiAu`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrFlSo`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrFlCx`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrFecF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrCtIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrObsT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPeCan`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPerCc`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEspSep`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrSedQ`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICitNum`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICitEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndOpu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuUso`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndRei`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRegOpe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecSR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRValAn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDurMn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDurHr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProVia`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProLat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResCam`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITipCam`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObRCam`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObsHD`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIReqHD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodHD`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDispEE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObsEE`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIReMaE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObMaE`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPreSe1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEspSe1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntHD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPObsHD`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProFoHc`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
