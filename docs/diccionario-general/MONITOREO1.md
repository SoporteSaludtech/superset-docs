# MONITOREO1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItmCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MonItmDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItmAbr`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItmOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`UnMdCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipMoFor`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonTipReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItmNeg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonUltLis`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
