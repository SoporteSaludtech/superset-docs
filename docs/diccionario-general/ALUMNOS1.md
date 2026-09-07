# ALUMNOS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AlumCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AlumEsp`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AlumFchIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumFchFn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumNotDe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AlumInCal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
