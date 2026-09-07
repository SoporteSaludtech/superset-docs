# PROGPYP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPPCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPPDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPDurMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPAyuRap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPEdaIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPEdInEn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPEdaFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPEdFiEn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPSexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPCNCCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPTipPro`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPITBC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPVIH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPNoRep`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PyPEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PyPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
