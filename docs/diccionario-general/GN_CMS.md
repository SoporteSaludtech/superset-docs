# GN_CMS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CMSID`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CMSEMPCOD`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CMSPRVCOD`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CMSMSRESO`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CMSCB`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
