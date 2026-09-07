# ATS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ATSNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSEst`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
