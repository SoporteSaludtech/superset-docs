# OPEBANCON1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MesMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AnioMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OBCCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`OBCCodOpe`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCOriOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCFecOpe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCDocRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCValOpe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCEstOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForConCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCMesCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCAniCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCDocNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCSede`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCUsuCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBCFecCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
