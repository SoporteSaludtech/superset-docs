# HOJOBLCXC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCDocObl`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCNumObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCCntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCtrcCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOCCsc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOCFchRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOCDocMov`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOCNumMov`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOCFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
