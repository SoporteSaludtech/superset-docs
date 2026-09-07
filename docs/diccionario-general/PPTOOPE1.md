# PPTOOPE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`VlrMov`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VlrEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalEmeEco`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalObsDet`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalSta1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalVlrAnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
