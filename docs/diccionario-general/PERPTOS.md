# PERPTOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CurCodCur`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CurSexCur`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PerCodPer`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PerPtoCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`PerVlrX`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PerVlry`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
