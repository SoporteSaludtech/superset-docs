# ADGLORA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlorCtv`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GlorNumFa`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GlorFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorSedRa`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorCueDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorCueCn`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorRegCn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorDesc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorNumDo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorTipDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorFecdo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUsND`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorFecCi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUsCie`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTotFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVltIv`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVltNe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUbiFa`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUsFa`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorPunRu`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorEstEn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorEsAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorUsAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorFHAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
