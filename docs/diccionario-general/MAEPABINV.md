# MAEPABINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNumC`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNCCtvIn`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCDesIn`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPNCCanIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCObsIn`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
