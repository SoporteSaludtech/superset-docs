# PLAEJETR1

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
| 🔑 | **`PleCnsCoR`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PleCnsCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleUlCnAc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitEmC`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitSeC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitNuC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEmpCot`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleSedCot`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCotDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCotCon`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNumFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleDocFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTieCiC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsFac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsCoC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTpoTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleIndTFa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTipLiq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTipLid`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLeCodPrC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTipo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEspPrC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTipPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNroAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNroCto`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleObsPro`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNumDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCarDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleFolOdo`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsPrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PlaPiOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleProGar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEstItP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleApyCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleIndCoM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleValCoM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleIndAdT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEREQAUT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLEDIAAPL`** | `numeric(4,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PLECODCIR`** | `int` | SI | Campo transaccional de Hosvital HIS |
