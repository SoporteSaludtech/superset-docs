# PEDPAQQX3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PaqCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PQCnsDes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PQTipTrn`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PQCnsLot`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQCodLot`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCOdPro`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQFchLot`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCntLot`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQMovLot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
