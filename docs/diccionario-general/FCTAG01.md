# FCTAG01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFCnsAgr`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AFClPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFFchI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFFchE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFFchS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFTotP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFTotS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFTotF`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFValS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVaAb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVAPU`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVPaU`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVDsc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVNPU`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFFecFIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFFecFFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFPabF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFUsuF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVALIVA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVALBAS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
