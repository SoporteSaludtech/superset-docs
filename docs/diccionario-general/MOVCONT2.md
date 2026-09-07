# MOVCONT2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CntVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRf1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRf2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRf3`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCVlrLc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCVlrEx`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDet`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCImpCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCSedOrg`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCAnio`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCmpAj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRf4`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRf5`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCntPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCGASDED`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCIDETRD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCFCHAUD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCNROAUD`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCImpPcj`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCAutRet`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNumRet`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
