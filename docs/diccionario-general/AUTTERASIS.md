# AUTTERASIS

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
| 🔑 | **`TerNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutNroFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutMaTipD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutTerSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutTerCod`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutTerCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutTerUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTerFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTerEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTerVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlrImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlrDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNroAbo`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDocPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNoPag`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNoCxP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDcCxP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDscDef`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFchCxP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlrGlo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFecAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTerPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMet`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFchCor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSAPErr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDocRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFecRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNroRad`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutSAPCm`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
