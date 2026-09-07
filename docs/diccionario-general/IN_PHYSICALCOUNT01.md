# IN_PHYSICALCOUNT01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CancelationDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`CancelationUser`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CreationDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`CreationUser`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdCompany`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdOffice`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdWarehouse`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Month`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Status`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Year`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
