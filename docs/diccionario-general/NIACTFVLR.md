# NIACTFVLR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIAFVRCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIAFVRNUE`** | `numeric(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIAFVRUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIAFVRFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIAFVRFMOD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
