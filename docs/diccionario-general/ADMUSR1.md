# ADMUSR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsPAuDto`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrEstDp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADMU_ID`** | `varchar(36)` | SI | Campo transaccional de Hosvital HIS |
