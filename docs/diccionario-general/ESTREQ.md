# ESTREQ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReqNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReqItem`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReqEstPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReqFchCam`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ReqObsItm`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqUsDMod`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqCntEnv`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReqMSReso`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
