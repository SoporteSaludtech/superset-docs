# BODEGAS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodUbiCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodUbiPas`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodUbiDIz`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodUbiNiv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BodUbiCtv`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodUbiEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
