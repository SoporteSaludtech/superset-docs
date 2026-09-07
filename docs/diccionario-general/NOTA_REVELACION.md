# NOTA_REVELACION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`codigo`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`descripcion`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`anio`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoNota`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`estadoFinanciero`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
