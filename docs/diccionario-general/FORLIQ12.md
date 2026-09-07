# FORLIQ12

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForLiqCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HnrCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForLqVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForLqEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ForCntUVR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForCntCos`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
