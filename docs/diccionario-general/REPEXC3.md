# REPEXC3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepClCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RepMas`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepTipDat`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepTipFil`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
