# PRVPROD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvPrc`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvUlPrcE`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvTpoEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCdFab`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCodEAN`** | `char(14)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSFctCnvE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVPRCDES`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVFCHMO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
