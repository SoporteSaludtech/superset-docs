# REICOM61

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PntCodi`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIFol`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIAntObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAnObFl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RNQCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAntPar`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndPat`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHC6`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoHC6`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
