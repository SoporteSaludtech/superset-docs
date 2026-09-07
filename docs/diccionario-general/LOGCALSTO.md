# LOGCALSTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FecAct`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogBodAct`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`UsuAct`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CalStoMin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CalStoMax`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
