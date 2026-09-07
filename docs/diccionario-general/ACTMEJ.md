# ACTMEJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ActMejCons`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ActMejDes`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejXDe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejObs`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejFUD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejFUA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejCH`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejDN`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejSD`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejPoA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejPoD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMAjxInCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMAjxInDp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFchUlDp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFCtoHis`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFDepN`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFSldDp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFAjCto`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFAjDp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFAxICto`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFAxIDp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFVidUt`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AMFOri`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejAvN`** | `decimal(16,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejAvD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ActMejAvS`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
