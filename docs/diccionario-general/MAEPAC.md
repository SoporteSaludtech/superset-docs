# MAEPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MTUCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MTCodP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNoCa`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCUOM`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPstatus`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPACMO`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`UltCtvPrx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPResExe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFchAfl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpPunSIS`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpFicSIS`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPoPla`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitCed`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitNom`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitCon`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MenTitular`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
