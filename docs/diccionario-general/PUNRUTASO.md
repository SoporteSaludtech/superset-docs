# PUNRUTASO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpCodOrPr`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SedCodOrPr`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PunRutOri`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EmpCodDePr`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SedCodDePr`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PunRutDst`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PunRutAsoC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PunRutAsoE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
