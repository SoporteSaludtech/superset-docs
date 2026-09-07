# CTRPRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrPreNoD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrPreCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTRPRESED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrPreCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrPreEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrPreTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrPreFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
