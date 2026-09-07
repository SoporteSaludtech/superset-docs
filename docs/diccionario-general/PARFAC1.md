# PARFAC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParFacTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParFacCVi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParFacCCA`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacDAu`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacCU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacSCU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacSCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
