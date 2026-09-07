# RESENCU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResDocPac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResTDoPac`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResFolPac`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResCtvRe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResFecHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResDxAs`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResEmpPyP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResSedPyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResPrgPyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResActPyP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResPrcCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResPrcCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResDocCon`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResMsCodi`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResMsPrAc`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResCncCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResMsform`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESFOLRES`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESMMCODM`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESMECODE`** | `int` | SI | Campo transaccional de Hosvital HIS |
