# SMOVINV3

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
| 🔑 | **`SDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SMvtCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtBdE`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtBdS`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FchSlct`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtDocPac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtTDoPac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtSubCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtDocRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SmvtDetEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtUsuaut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtFchAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtBdRef`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtVURm`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtItmRq`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvTipDsp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMSpsErr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMSpsCnf`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvUbCEnt`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvUbCSal`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtVU`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtVM`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtIU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCaNeg`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvNegBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvNegUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvNegFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvUsuUso`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
