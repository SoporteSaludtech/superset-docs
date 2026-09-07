# CHEQUERA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CheNro`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CheNoIni`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheNoFin`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheNoAct`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCVigTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCTESCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODTRN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheUsrCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheUsuUni`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CheTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
