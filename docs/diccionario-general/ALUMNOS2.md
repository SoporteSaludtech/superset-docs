# ALUMNOS2

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
| 🔑 | **`AluFchExp`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AluEspExp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AluFFinExp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AluTipExp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
