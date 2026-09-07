# ENTTURN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TurCod`** | `decimal(12,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TurUsrEnt`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurFchEnt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurUsrRcb`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCjCod`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurvlrTot`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurCJSCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
