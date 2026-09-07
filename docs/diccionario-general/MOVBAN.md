# MOVBAN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvBNroCmp`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvBCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvBFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BANCOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBMonBse`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBTasCmb`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBCpt`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBNumChq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBNCheqr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBBenChq`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBTipMov`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBVlrEx`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBConBan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBBanCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBDepCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBCiuCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBEntChq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBDocPos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBFchPos`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBCodAut`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBAntApl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCTESCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODTRN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRITipOp`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBDet`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBDocDet`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBConTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBTipRc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBCodCon`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBConDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsLote`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCVigTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBSedDet`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvBVlrBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVIndAnuD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvEstRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvEstUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsNroPlC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBID`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstadoCorreo`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
