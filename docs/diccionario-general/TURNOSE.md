# TURNOSE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TurEsp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TurDscEsp`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
