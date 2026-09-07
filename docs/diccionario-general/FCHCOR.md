# FCHCOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FchCorAni`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FchCorMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FchCorOpo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FchCorRe1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FchCorRe2`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
