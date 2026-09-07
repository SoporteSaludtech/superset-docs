# CTRCSTPRM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CCPCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CCPMsReso`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CCPDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPNroDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPMovCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPBodega`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPTipMov`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPUsrMov`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPVlrUAn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPSldUAn`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPCstPAn`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPSldUMo`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPVlrUFi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPSldUFi`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPCstPFi`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPVlrUMo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPCSPFIN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCPCSPANN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
