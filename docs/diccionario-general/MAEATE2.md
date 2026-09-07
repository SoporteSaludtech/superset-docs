# MAEATE2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MACscP`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRCODI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaHonCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MATipP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MADiPr`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ViaCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAFePr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MADiPP`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAProc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPerA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECoMM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MADiCo`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAVaTP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MANumAS`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAConP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MACodCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUPro`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAFPro`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAHPro`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDi1S`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDi2S`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDi3S`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCAUE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTIPD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCanPr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPInte`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPOpcn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPVias`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPEspe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNGrp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCodi`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPpcso`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPpHoMe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPpInte`** | `decimal(13,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTipD2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTipD3`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPVLRUVR`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPUVRCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTpco`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTPMo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPmHoMe`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mpvrpu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mpftrv`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFINA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPNDCT`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCITA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPRiad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FcPCodCCs`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FCPCodSCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FcPTpoTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaNumFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaUsuAnl`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaAgrCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaVlrTot`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaNomA`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaOrdLiq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaPorImpt`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCanPe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCnsAQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodCam`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaEsParXTo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaEsAnuP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCoReca`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaConPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaIndCop`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodPar`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaEsPAnuP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaNumAuE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCtvEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCanCa`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaOrdMan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCscSAgr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MapPorIva`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MapVlrSIv`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAECODPQT`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MATIPLIQP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPRODSC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MFFchAnu1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaCodAnuP`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODFINA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAIMPPRC`** | `numeric(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MACODIMPP`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEtEnT`** | `numeric(1,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPCODHOM`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPCTEPAQ`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPCNSPAQ`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPIDMIPR`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPAUTPRO`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodMAte`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MServCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
