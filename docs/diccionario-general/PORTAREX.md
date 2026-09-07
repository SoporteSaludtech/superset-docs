# PORTAREX

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PTCodi`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PtExInFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExVlDif`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExCoTar`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExPorBa`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExCoFac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExForLiq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PTExCnUvr`** | `int` | SI | Campo transaccional de Hosvital HIS |
