# CALFCRPRE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRECOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CALPRECOD`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CALVIG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CALPREDES`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CALPREPON`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
