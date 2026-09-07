# LOGCIEPER

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogCieAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogCieMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogCieCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`LogCieUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogCieTMv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogCieFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
