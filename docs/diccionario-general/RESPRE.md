# RESPRE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESPRESEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESPREDES`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESPREEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESPRETIP`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
