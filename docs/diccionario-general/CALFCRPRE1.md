# CALFCRPRE1

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
| 🔑 | **`MAEINDCOD`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAEINDNUM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEINDDEN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEINDFTR`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
