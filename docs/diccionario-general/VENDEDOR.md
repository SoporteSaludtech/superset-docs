# VENDEDOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`VenNum`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`VenNom`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VenAnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VenAct`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
