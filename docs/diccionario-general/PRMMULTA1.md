# PRMMULTA1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmEsp`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrMClaCit`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrMCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrMFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrMVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrMNroMul`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
