# AUDFORPRE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AudForCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPreCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPfoOrd`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPfoFhc`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPfoUcr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudForObs`** | `char(240)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPfoSec`** | `int` | SI | Campo transaccional de Hosvital HIS |
