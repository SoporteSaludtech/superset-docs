# CHEQUES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CheNro`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ChqNro`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ChqEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ChqObsAnu`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ChqFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ChqUsrMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
