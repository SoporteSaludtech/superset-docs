# AFVLRRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ACFVRCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ACFVRNUE`** | `numeric(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACFVRUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACFVRFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACFVRFMOD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
