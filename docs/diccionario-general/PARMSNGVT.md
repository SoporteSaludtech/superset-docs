# PARMSNGVT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ParCodSgv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParObsSgv`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParTipSgv`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParEdaInc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParTipInc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParEdaFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParTipFin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParRanInc`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParRanFin`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFecCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFecMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParPerAbM`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParPerAbF`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
