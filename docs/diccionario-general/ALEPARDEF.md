# ALEPARDEF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParPorDef`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParParDef`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParMenDef`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParDilDef`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParTieDef`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
