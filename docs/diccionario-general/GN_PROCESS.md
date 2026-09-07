# GN_PROCESS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IdType`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Request`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Response`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdPrefix`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdRecord`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdStation`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdUser`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdParent`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcDate`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
