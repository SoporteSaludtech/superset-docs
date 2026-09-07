# MDPCLADEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpClaCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpClaDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpClaSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpClaVin`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpClaVfi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
