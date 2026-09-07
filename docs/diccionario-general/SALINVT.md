# SALINVT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalCrr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUndAnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUndEnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUndSal`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalUnd`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalCstPrm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalCsgn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalVlrEnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalVlrSal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SALCSTPRN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
