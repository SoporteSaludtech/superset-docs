# HOJOBL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HojNumObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchObl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojVlrCuo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojCuoIni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojVlrObl`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojTotCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojTotDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojTipPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojTpPgDs`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNumCuo`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNroRem`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchRem`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNroRad`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojTipGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojStaGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFchRecGl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HjFchRadGl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HjFCanObl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojVlrGlo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOIndDev`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HONoRadG`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojMaTipD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNroCas`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojCarRch`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchRch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojUsrRch`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojIndFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojDocRes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNomRes`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojApeRes`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojCnsIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojEstHom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojIndRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchRaR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNumRaR`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojUsuInf`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchInF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojIndInF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojOblClU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojOblClF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojOblClE`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
