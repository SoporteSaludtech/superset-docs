# LOGSINAD1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogSADCtv`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogSADIde`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogSADTId`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LogSADDes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
