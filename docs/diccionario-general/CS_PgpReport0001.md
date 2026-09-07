# CS_PgpReport0001

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`criticityLevel`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idContract`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idProcedure`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idUser`** | `varchar(75)` | SI | Campo transaccional de Hosvital HIS |
|  | **`procedureCount`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`procedureDescription`** | `varchar(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`unitValue`** | `numeric(18,2)` | SI | Campo transaccional de Hosvital HIS |
