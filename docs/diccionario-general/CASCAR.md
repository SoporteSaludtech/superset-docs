# CASCAR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CasCarDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CsCrNDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CasCarEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CasCrFchG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CasCrFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CasCarUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrUltCns`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
