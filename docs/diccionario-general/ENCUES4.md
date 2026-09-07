# ENCUES4

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
| 🔑 | **`EncItmPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncItmCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EncItcDsc`** | `char(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncItcOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncCtCoRe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncEspAd4`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
