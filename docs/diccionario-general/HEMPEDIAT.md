# HEMPEDIAT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMPEDCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMPEDPRC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HEMPEDORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPEDFIL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPEDFDE`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPEDTAB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPEDFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPBAS`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPBASE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPBAST`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPCONO2`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPCONO2E`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPCONO2T`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPST21`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPSTO2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRTD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRMED`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRSO2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRDO2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRTDO2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPPRMEO2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMPTDATO`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
