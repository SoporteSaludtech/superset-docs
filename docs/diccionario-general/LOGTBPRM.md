# LOGTBPRM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LTPCodTlb`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LTPCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`LTPFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPATrMod`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPVlrAnt`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LTPVlrAct`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
