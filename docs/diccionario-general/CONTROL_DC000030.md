# CONTROL_DC000030

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`anio`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`trimestre`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`esInicial`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaEjecucion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`usuarioEjecucion`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
