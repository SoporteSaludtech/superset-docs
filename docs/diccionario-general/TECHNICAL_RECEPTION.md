# TECHNICAL_RECEPTION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_company`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`quantity_min`** | `decimal(17,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`quantity_max`** | `decimal(17,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`quantity_sample`** | `decimal(17,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`status`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
