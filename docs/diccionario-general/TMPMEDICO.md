# TMPMEDICO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TMmCodm`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TClapro`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TTpPrcod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMaFePr`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TVlrProc`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TvlrHono`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCntFct`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TMdAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
