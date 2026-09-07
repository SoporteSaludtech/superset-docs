# REQUISI1

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
| 🔑 | **`ReqItem`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqNomPro`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCanApr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqGrp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCanEnv`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCanNeg`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqOrdCom`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqPrvDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqPrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUndCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCarPro`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CauCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUltEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqSedOrC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqDocOrC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqNroSol`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqEnvCmp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCanPA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUsuApr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqFecApr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESOSus`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodLote`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqVlrUni`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
