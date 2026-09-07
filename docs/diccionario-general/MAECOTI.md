# MAECOTI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConse`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotAten`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPabe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotFecVig`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCont`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTUCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTCodP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotObser`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEsta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEsAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCam`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCnsOrQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUltCoP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUltCoS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUltCoC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotMeCoPa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotMeCoMo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotMeCaPi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVltCoP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVltCoS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVltCoT`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVlrSub`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVlrPxU`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPtCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPsCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotDesc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPorCIn`** | `decimal(9,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotFecCIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotFecCOr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotNumCIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotNumCOr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValCIn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValCOr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCnsUlt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
