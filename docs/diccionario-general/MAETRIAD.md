# MAETRIAD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaeCodPaD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DiaCodGru`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaeTriDiD`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaeHorIni`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaeHorFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
