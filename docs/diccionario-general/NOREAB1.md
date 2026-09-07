# NOREAB1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NReaNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NReaCanSg`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NReaCanRb`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MtRchCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
