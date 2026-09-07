# DEPMEJACT

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
| 🔑 | **`DMAcAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMacMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DMAcCtoHi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMAcVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMacAxI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMACCtoAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMAcDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMacDAxI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMAcDAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMAcIndCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
