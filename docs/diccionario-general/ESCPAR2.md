# ESCPAR2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ESCCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ESCCODDET`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ESCCODIND`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ESCDESIND`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCPUNIND`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCORDIND`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESPINDIMA`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCSUBGRU`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
