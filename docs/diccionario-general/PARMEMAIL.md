# PARMEMAIL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`mcdpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipo`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`remitenteEmail`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`remitenteEmailPass`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`firmante`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cuerpoEmail`** | `text` | NO | Campo transaccional de Hosvital HIS |
|  | **`asunto`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`serversmtp`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
