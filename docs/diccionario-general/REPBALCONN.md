# REPBALCONN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepBalMed`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepBalNum`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepTotCod`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepSubCod`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepConCod`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RepConDsc`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepConOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepConInd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepcConCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepConCapD`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepBalSum`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
