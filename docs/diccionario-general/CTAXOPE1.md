# CTAXOPE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxOTipOp`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxOProc`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxOClsRub`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxOCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CxOClsRD`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxOCntDeb`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxOCntCre`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
