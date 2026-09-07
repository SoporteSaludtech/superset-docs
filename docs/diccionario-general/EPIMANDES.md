# EPIMANDES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EpiCtvo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EpiDesAtr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EpiDesDet`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
