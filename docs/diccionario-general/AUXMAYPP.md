# AUXMAYPP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RubPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RubPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AxMaPPMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AxMaPPValR`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AxMaPPValP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
