# CMPPRE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgCCdg`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgCCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDocRf1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDocRf2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDocRf3`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDocRf4`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCPrj`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCOtr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDet`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCSedOri`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
