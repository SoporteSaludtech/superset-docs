# MONGRAREC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GraRecCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`GraRecPre`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GraRecHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
