# CRUCTATAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HojNumObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CruSedObl`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CruCtaCon`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruUsuAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruFchAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruCtaVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruCtaSal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruCtaEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruNroAut`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
