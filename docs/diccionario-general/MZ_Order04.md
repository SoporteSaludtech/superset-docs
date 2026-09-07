# MZ_Order04

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`newQuantity`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`oldQuantity`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`updateDateTime`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`updateIdUser`** | `varchar(75)` | SI | Campo transaccional de Hosvital HIS |
|  | **`updateObservation`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOrder02`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
