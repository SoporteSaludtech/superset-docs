# REICUIEN1

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
| 🔑 | **`CuiEnfCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CuiFaRCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICuiFr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICHorIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuiObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuiPa1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
