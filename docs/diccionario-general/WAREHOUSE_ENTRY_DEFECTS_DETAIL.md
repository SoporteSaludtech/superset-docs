# WAREHOUSE_ENTRY_DEFECTS_DETAIL

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
|  | **`entry_detail_consecutive`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`id_product`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`consecutive`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`classification_defect`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`id_warehouse_entry`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
