# AUCCON13

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
| 🔑 | **`AudForCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPreCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPrtCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AuCCCsc`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AuCCTera`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCConObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCVaR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCInst`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCEd`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCcCur`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCTip`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCTiem`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCTieTr`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AuCCAv`** | `char(400)` | SI | Campo transaccional de Hosvital HIS |
