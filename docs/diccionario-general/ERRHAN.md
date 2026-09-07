# ERRHAN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ERRFECHOR`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PROGRAMA`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ERRN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GXDBERR`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GXDBTXT`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GXOPER`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GXERRTBL`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GXERROPT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENSAJE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
