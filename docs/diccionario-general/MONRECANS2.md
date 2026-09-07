# MONRECANS2

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
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItmCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonRecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`MonRecAnsV`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonReEsD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
