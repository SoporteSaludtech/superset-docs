# AMOACTDEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcDCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AmorAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AmorMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AmoCosHis`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmoCoHiAn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmoValMes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmoAcuAct`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmAjxIMCH`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmAjxMes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmAjMCHAcu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmoIndCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AmoBseAmo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
