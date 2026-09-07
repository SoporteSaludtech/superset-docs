# PPTOOPE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocCodRef`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocConRef`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocSigRef`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocRefOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalDebCre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalObs`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalHorCre`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalHorMod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalEstCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstAfecPre`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VigEstAfec`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocReOcNo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalMesS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalMesSta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodAuxReg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocReSeOC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
