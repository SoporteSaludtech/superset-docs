# NOTATEC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NTCNS`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`NTPROEJE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTPLAOBJ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTPLACLA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTPERINI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTPERFIN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTDPT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTCIU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTCANPRO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTCANSER`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NTCANDIA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUTOTPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPCUPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPCANPRO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RECUPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RECANPRO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUDESPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUTOTSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPCUSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPCASER`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RECUSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RECASER`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUDESSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUTOTDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RPCUDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RECUDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CUDESDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PEPOR`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PEPER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PECAN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PEPRO`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`FUUPER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FUUPRO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FUUSER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TDEDAD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TDSEX`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TDGRUETA`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TDMARRIE`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`IBPPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IBPSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IBPDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTUPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTUSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTUDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CAUVALCOS`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CAUCOSADM`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CAUPORTAR`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`CAUPORTOT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CVUVALCOS`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CVUCOSADM`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CVUPORTAR`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`CVUPORTOT`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MUUVALOR`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MUUPORBAS`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MUUPORTOT`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTTPRO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTTSER`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VTTDIA`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
