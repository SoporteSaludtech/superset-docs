# MDPGRACOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpGraCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MDpGraDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraEdI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraEdF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraVin`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraVfi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
