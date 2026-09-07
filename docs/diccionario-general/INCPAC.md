# INCPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IncEmpPac`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncSedPad`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncConPac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncDocAfi`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncConIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncConAcc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLugAte`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFecIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDiaInc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFecFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDiaPri`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCodAfi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncSOAT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncTipReg`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCodEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCodFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncProAfi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDiaAcu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncEdaGes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncTipAte`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncSipErr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCscCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncNumAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCon`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCenAte`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFchAcc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncTipPro`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncObsMed`** | `char(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncEstInc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncCodCan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncObsCan`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFecCan`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncIndRet`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncModSer`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDiaRln`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MOCodPri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncConSin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncTelTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncMotExt`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncPrCodi`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncDisPac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncSubLic`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncFeEnMe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLicExt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLicCom`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLinFle`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLicOtr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncLicCui`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncReposo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IncHorRep`** | `numeric(4,0)` | SI | Campo transaccional de Hosvital HIS |
