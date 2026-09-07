# sysdiagrams

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`name`** | `sysname` | NO | Campo transaccional de Hosvital HIS |
|  | **`principal_id`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`diagram_id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`version`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`definition`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
