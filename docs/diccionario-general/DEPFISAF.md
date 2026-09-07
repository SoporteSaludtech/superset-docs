# DEPFISAF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DFisAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DFisMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DFisCHis`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisAxI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisCtoAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisAjxID`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisAjDp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisInCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DFisBseD`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
