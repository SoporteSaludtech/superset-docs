# MDPCLARIE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpRieCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpRieDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRieSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRieVin`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRieVfi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
