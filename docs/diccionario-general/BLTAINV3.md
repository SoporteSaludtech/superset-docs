# BLTAINV3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BltSldUnd`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltCstPrm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltCntNo1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltCntNo2`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltCntNo3`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltDifNo12`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltCntDef`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltProAjs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltDifLot`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltIndCi3`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltDifLoU`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltDifUbi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BLTCSTPRN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
