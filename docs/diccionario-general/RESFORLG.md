# RESFORLG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`codResol`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RFLOGSEC`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESSEGSEC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESPRESEC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFLOGEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFLOGFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFLOGUSR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
