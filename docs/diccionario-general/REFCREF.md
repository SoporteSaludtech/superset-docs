# REFCREF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RefCod`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RefTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RefNom`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefCelRef`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefTelRef`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefIndRef`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefExtRef`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEcntr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefIPSRef`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDscDx`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDscSrv`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefVlrSrv`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefIPSRcp`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefAutCod`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefFchRms`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefIndAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefTpoAmb`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefFchIng`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefTipAte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMCodi`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RefRegRef`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefFeHTrs`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDocEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefRegEnt`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefNomEnt`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDocRec`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefRegRec`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefNomRec`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTUCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTCodP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDocRes`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefTDoRes`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDpoRes`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefMunRes`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefNomRes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefDirRes`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefTelRes`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefParRes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefCscIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefMotNeg`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefNivCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefCauExt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefConRef`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefMotReM`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFMEDREF`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFUSUACR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFFCHACR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFUSUREC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFFCHREC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFUSUANU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFFCHANU`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFOBSCRE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFMEDREC`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFMEDENR`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFORGREF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFESPREF`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REFCODRCH`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFMOTRCH`** | `char(256)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFSUBTIP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFCODERE`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFESPRCP`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFMOTRDE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFHALREL`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPDIA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFDMCOD2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPDIA2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFDMCOD3`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPDIA3`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTRAEJE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTRAREC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFJUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPATS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFPRIATE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFSERSOL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFLisDev`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFNDOREC`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTDOREC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPCAT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
