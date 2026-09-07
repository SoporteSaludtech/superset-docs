# OBJECDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ObjDetSec`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ObjCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPlaCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODTipItm`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODValGlo`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODCanGlo`** | `decimal(12,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODValAce`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODValSop`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODFecRes`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODUsuRes`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODObsrv`** | `varchar(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GlsCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODItmObj`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODNumOrd`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ODTipOrd`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ODConMae`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ODObsRes`** | `varchar(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MtvGlsCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ODMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ODIndTer`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ODEstRes`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
