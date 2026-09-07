# MAECJS2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CJSCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CJSCons`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CJSUsrAcc`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CJSFIUso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CJSFFUso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
