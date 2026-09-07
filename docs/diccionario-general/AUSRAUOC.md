# AUSRAUOC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AusrTpA`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AUsrAuCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AUsrFchAc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrFchIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrMtoAu`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrAuEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
