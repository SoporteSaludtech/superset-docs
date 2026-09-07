# RESSEG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESSEGSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESSEGDES`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESSEGEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESSEGHC`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
