# GLOSARADC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`GlsRaCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlsRaEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlsRaViCu`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GlsRaCue`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
