# ENVHRF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EnvNroF`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EnvPuRuOF`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUsOrF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvFeOrF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvPuRuDF`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUsDeF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvFeDeF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvEsCoF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvNrOrF`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvCabObF`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvSeDeF`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnTiTrF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
