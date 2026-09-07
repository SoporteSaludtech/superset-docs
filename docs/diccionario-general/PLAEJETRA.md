# PLAEJETRA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleCnsPtR`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PltCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PleFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleFchOr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrId`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PlePabe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCont`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleUltCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTUCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTCodP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleUsoInd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleUsoUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTipPla`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTarPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleConPar`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEmpCit`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleSedCit`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNumCit`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleSedPla`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEFCHEST`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEUSUEST`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEMOTCIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEOBSCIE`** | `varchar(8000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLECODESP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLECODMED`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEONCESQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEPRTCOD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEPRCESQ`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEINGORP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEATEFAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEPABFAC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEOBSPLA`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
