# ENCUES2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncAgrPr`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EncPreDsc`** | `char(600)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncOrdPre`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncUlCIt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncEspAd2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncSepSiP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncEsMen`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncColGri`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncAgrSec`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
