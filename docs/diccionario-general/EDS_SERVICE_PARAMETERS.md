# EDS_SERVICE_PARAMETERS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`idCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`provider_service`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`url_service`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`json_params_body`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`environment_service`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`name_service`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`type_service`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`json_params_header`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
