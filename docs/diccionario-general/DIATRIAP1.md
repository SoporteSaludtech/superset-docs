# DIATRIAP1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DiaCodDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DiaCtvEda`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaEdIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaEdInE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaEdFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaEdFinE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
