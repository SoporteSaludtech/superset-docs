# UT_PROCESSCONTROL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`code`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`finalDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`idCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idType`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idUser`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`initialDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`result`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
