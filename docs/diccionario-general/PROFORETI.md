# PROFORETI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`GRUFORCON`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PROFORCON`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PFECON`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PFEDES`** | `varchar(150)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PFETIP`** | `varchar(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PFEFUN`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PFEORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PFEEST`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
