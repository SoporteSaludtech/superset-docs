# KARDEX2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocTip`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovCsc1`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovLote`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVgc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCntL`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovNroRq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovFecReq`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
