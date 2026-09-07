# ADMGLO01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AGlEmpCd`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlMcdpt`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlDocCd`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlRemNr`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`EmprNit`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRemFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRemHr`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRadNr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRadFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRadHr`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRadCn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRadVr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlRemEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglUsrIng`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglUsrAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglDscAnu`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglEveGe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0009`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGLREMANP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
