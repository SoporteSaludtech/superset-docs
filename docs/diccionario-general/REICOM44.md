# REICOM44

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIDIETCD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIDieDsc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDIEEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEvCoEn`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEvObEf`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEvFHEf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITipRD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHC4`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoHC44`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
