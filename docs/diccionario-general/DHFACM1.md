# DHFACM1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DHAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHCenCo`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHTipCo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHMeNit`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHSbCos`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHCPCos`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DHLPa1N`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPLPa1N`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBF1PP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBF1SP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBF1PU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBF1SU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBF1PP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBF1SP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBF1PU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBF1SU`** | `int` | SI | Campo transaccional de Hosvital HIS |
