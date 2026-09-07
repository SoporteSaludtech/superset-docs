# MZ_Order01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`creationDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`idCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOffice`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOrder`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idUser`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
