# REDIATMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`RediUsu`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediMecn`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediMenn`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediDiag`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediTipDo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediTip`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediOri`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RediCHon`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RediNuReg`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RediCant`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RediVlr`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RediTTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
