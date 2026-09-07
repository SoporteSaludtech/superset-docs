# CTAPAGOPE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxCPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxCPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PagVlrMov`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagVlrEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagSta1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
