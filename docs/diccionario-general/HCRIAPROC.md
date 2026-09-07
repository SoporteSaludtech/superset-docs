# HCRIAPROC

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
| 🔑 | **`HRIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAPrCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAPrCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrDet`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRiaPrFre`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrCtC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrTAct`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrRqOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrRqFC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrRqAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIArSAPre`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrRAg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrTAg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrPrRe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrPrOr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPrAsFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPROrFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPRApFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRIAPrFOr`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRIAPrFAp`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPEsAsg`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPEsOrd`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPEsApl`** | `decimal(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPAtAsg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPAtOrd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIAPAtApl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
