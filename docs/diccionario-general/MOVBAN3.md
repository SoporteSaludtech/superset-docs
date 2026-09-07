# MOVBAN3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MVB3CON`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MVB3DOR`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3NOR`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3ID`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3DDI`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3NDD`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3NAN`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3DAN`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3FEANU`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB3USANU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
