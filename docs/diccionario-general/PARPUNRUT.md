# PARPUNRUT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpDocEnv`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocEnvPD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocEnvHC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocEnvND`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
