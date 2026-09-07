# MOVINV4

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtoCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoBdE`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoBdS`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FchMvt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVtoCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoDocPac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVtoCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoSubCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoDocRf`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoCUnC`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoVlU`** | `decimal(16,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoVlr`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoSld`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoInd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoTDoPac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoAnio`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVlrIVA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoIndLt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoUCEnt`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoUCSal`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoFolPa`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoNrAut`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoReqN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoCnsRq`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoSolN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoNumFa`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoTipFa`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoReqEm`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoReqSe`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoReqDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoTDoRe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoOrMov`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTOVLRNI`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTOVLUNI`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoEntNo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoEntDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoEntSe`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoNroSe`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoOriBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoOriCns`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoPorIv`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
