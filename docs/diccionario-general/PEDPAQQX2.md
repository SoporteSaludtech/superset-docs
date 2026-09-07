# PEDPAQQX2

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
| 🔑 | **`PQCvoDes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQTpoTRN`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQFHMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCntMov`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQUsrMov`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCodDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQNumDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSedMov`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQPabellon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PqPadCed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQBodDes`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSpsNL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
