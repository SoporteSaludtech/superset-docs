# WAREHOUSE_ENTRY_DEFECTS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`id_company`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`id_office`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`id_document`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`entry_number`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`number_minutes`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`status`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`carrier`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`guide`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`novelty`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`defect_observation`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observation_adminstration`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observation_technical`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`user_create`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
