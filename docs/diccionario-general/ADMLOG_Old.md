# ADMLOG_Old

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ALogSysId`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ALogPgmId`** | `char(11)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ALogEvnId`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ALogUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ALogWrkSt`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ALogCst`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ALogDT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ALogTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ALogObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
