# MAEDIL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DILCSC`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`DILDSC`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILPSI`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILPSF`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILDOS`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILFRC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILMSCODI`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILMSPRAC`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILCNCCD`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILMSFORM`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILCAN`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILUND`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DILLINPROD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
