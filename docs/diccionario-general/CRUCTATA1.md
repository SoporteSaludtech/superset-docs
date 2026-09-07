# CRUCTATA1

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
| 🔑 | **`AutTerCod`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CruVlrDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruCtaUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CruCtaFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
