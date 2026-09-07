# CTAPAGOPE

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
|  | **`DocPagRef`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocPagRNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocPagCE`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocPagNCE`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagObsOpe`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagHorCre`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagHorMod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagStaCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagEstAPre`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
