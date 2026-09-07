# KARDEX

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MovStkMin`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovStkMax`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSUCs`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSUni`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSVlr`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCUni`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCstP`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovUltCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCnsP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCnsPD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSolRea`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MOVCSTPNI`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
