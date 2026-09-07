# PEDPAQQX1

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
|  | **`PQCaSuSl`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCaSuDs`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCaSuDv`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCaSuUs`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQFecHDes`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQUltCtvo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQEdoIte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCaSuUsP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQFolPro`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQEstDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQEdoCaI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQConTipI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQConCodI`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCaSuPe`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQAplSum`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQAplFHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQAplObs`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQAplUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQMSRESOH`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
