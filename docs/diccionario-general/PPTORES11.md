# PPTORES11

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
| 🔑 | **`ResPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResPreNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResVlrMov`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResVlrEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResSta1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
