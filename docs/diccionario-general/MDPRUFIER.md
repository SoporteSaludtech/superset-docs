# MDPRUFIER

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpRufCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpRufDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRufVin`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRufVfi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
