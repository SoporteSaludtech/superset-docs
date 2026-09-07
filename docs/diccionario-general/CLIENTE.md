# CLIENTE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CliFacOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliPlzPar`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLIDCPLZC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliMedPag`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliFrmPag`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
