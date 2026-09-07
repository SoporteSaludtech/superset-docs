# DEPMJFIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ActMejCons`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMFisAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMFisMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DMFCtoHi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFVlrMej`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFisAxI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFCtoAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFisDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFAxIDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMFAjDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
