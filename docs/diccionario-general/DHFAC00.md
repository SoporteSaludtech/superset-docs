# DHFAC00

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DHAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHCenCo`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHMeNit`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHTipCo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHSbCos`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DHCPCos`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DHLPacN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPLPacN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBFcPP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBFcSP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBFcPU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHBFcSU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBFcPP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBFcSP`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBFcPU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHPBFcSU`** | `int` | SI | Campo transaccional de Hosvital HIS |
