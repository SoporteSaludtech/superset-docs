# REICOM5

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIPrcTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrStGr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICPCan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICpObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrAutNo`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrAutNr`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REItvIn5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICCtvEn`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICscCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrcUsC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrcFHC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICaIntL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDosCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDosLot`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICDiaPT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHC5`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoHC5`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
