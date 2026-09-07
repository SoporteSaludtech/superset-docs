# COTIZAC1

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
| 🔑 | **`CotNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotItm`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CotMsRe`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotMsNoGen`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUndCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUndDsc`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotTpoEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MarCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotDscPrd`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPre`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotDes`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotIva`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotItmEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotSelCom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
