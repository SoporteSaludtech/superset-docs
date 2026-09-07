# MAERES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MAERESEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAERESSED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAERESCOD`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAERESDES`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAERESVER`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAERESEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAERESPER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAERESRSP`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
