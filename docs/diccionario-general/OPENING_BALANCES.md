# OPENING_BALANCES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`doc_cod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`doc_name`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`total_value`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`date_process`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`create_at`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_company`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_office`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_store`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`doc_number`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_user`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`status`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
