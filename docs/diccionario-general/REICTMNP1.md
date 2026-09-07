# REICTMNP1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTDoCo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTCtPO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICTCMCo`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTCaPO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTDoDi`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTPoso`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTPrAc`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTTiDu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTPrMe`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTCnCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICTCoPr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
