# DEFECT_LEVEL_ONE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`code`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_company`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`description`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
