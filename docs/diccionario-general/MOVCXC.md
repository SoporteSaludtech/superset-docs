# MOVCXC

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
| 🔑 | **`MvCxCNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCCCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCCFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxCMon`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxCTas`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCNumObl`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICOD`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCCnc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCCDocFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCliRcl`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCntRcl`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
