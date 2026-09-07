# GRAFICAREC

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
| 🔑 | **`GRACSC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GRAIMG`** | `text` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRASVG`** | `text` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRAFECINI`** | `varchar(19)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRAFECFIN`** | `varchar(19)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRAUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRAESP`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRATIPREP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
