# MOVBANCON1

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
| 🔑 | **`MBCDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MBCNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MBCSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MBCCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MBCOriOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCFecOpe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCDOCRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCValOpe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCEstOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForConCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCMesCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCAniCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCCodOpe`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCUsuCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCFecCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConManCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCPrcTes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MBCCodTrn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
