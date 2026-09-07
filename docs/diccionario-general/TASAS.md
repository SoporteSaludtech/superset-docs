# TASAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgrAsCd`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TasCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TasDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TasFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TasFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
