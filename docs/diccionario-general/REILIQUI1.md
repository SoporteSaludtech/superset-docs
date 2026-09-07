# REILIQUI1

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
| 🔑 | **`REILqCstv`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REILqHoRe`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REILqFeRe`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`REILqCnFo`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHorInD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqFHoR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqFeHR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqCnAp`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqUsRe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolReg`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFEsFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqCsH1`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqPa1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqFoH1`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
