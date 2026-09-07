# REICTCMND

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTDoCo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICTCDAt`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICTCDDe`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
