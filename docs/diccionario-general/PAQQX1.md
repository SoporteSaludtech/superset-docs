# PAQQX1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PaqCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PaqCant`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
