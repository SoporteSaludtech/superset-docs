# GD_F02

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`GD1ID`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GD2ID`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GD2FILE`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2EXT`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2NAME`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2USER1`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2DATE1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2USER2`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2DATE2`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2STATUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GD2TYPE`** | `int` | SI | Campo transaccional de Hosvital HIS |
