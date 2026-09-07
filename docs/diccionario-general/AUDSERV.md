# AUDSERV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutClaPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutIngCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMPCodP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMPNumC`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFecSol`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutHorSol`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFecFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutHorFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEstado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutObs1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCscCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNum`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNitSol`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutUsrCan`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMtvoCan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutObsCan`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlrExe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSrvNro`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutPtoAtn`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutPtoTer`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDiaCS`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutIndOri`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutPorSA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecTi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCuo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCop`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecOt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutReOtD`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCuV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCoV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecReV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecOV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCuM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecCoM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecReM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecOM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecPCu`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecPCo`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecPRe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutRecPOt`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerTAu`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerIAu`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerEAu`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerNoR`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerTR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerIR`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerER`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerCR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerCaR`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerCaA`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSerCel`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEstEnv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTFINTEC`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTMODREA`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTGRUSER`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTTIPSOL`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTPRIATE`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTDIAREL`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
