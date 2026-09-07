# HCANTE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AntTipCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AntAyuCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OBSERANTE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CALANTEC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntTuber`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntSinRes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntLepr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCulTraL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntResNFum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntResIPA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntAnosFum`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNoCig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CREENCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntVncFml`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTFECEPR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTFECAPR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntPreRN`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntRepApl`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTRAZNR`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
