# REICUIENF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CatCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICFecIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICUsRgI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICFecFi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICUsRgF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuiEdo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICNumDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICEstFo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObsPl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuiPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
