# MZ_Order06

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`idExternal`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStation`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idType`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idUser`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`processDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`request`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`response`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOrder01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
