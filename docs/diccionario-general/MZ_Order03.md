# MZ_Order03

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`idLocation`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idProduct`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idProductAlternative`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`lotCode`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`lotExpirationDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`idThird`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`requestedQuantity`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`authorizedQuantity`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`usedQuantity`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idRequest`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOrder01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
