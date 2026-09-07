# COMPCAB2

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
| 🔑 | **`OrdeNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OrdeCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeConc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeRcb`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeVlrU`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeVlrI`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeVlrD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeMFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdePlzEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeEstD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdReqNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdReqItm`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeBdg`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeTtal`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeTotI`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeTotD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdFchCau`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdEstCau`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdDocCau`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdReqSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdReqDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdIndPPt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdDcCau`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdSedCau`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPorImS`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTotImS`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
