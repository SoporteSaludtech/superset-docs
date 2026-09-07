# DSPFRMC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSmTpoTrn`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSmCnsMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DSmFHrMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmCntMov`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmUsrMov`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSCodDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsNumDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsSedMov`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsPabellon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCtvIn1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsEstRcb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsFchRcb`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsUsrRcb`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCnsDsp`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmObsRem`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmTipDsp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DspVlrDsp`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsBodSal`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSSpsNL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmMotDev`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsIMFID`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
