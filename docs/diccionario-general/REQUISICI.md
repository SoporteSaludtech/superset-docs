# REQUISICI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReqNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ReqFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReCnCCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RecCnCdDes`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqObs`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUsuCod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqSitEnv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUltItem`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqBodOrg`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqTrnCod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdPrc0003`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqDepId`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
