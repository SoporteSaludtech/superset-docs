# SOLINTSEG2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocInt`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FecHorObs`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstAct`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ObsEst`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuCam`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
