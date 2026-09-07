# PPLAHIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PpHiVer`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPlaCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PphiSec`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PphiFec`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`PphiUsu`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PpSdtHis`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPTipSop`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
