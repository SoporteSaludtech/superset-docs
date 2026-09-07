# REPBALSUB

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
| 🔑 | **`RepTotCod`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RepSubCod`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RepSubDsc`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepSubNot`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepSubOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RepSubSN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
