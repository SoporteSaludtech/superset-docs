# DEFECT_LEVEL_THREE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`code`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`description`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`status`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_defect_classification_two`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
