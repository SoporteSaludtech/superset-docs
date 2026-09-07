# MAEIPSAT2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IPSCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPSCons`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IPSEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IPSSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECodE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
