# RIAINST

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAESCCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAESCCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCNOM`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCPSex`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCEI`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCEIn`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCEF`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCEFn`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIASESCEst`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCAPLM`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAESCAOPC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAESCDIAS`** | `int` | SI | Campo transaccional de Hosvital HIS |
