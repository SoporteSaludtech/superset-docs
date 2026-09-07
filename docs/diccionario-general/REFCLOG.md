# REFCLOG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REFCOD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RFCLOGSEC`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`RFCLOGOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFCLOGUSR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFCLOGFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
