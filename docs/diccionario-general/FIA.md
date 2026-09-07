# FIA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`FIAEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FIAMCDPTO`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FIACod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRCODI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMCodi`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIAMUN`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIADEP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIAFECINI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIAFECFIN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACITA`** | `numeric(9,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACITAFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACITATEs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACITAFcS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACITAFcA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACIRCOD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACIRCAN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACIRCCAN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FIACIRMCAN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
