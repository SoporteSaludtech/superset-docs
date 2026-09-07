# TMPORD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpBodega`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpUsuCod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpMsReso`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpReqNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpReqSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpReqItm`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpPrvcod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpReqCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpUndCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpVlrReq`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTipRq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
