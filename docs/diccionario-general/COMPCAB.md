# COMPCAB

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
| 🔑 | **`OrdeNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OrdeFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTipCPlz`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTipDPlz`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTrnCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeDsc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeDTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeNFct`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeFchF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeUso`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeUsuC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeUsuA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeRecb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeUltCs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeAntc`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeCodBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeTotCDP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdEstPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeFchAu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdPrc0002`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPosVal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ORDENROEXT`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
