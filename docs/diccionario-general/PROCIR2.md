# PROCIR2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PersCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PersTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PersEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PersEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
