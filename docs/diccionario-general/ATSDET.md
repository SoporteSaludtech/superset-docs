# ATSDET

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
| 🔑 | **`ATSCsc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ATSVen`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSTipIde`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSTipEmi`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSTipCom`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSTipCli`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSRenRet`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSRazSoc`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSParRel`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSNumIde`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSNumCom`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSIvaRet`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSIvaCom`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSIva`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSICE`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSForCob`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSCom`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSCodEst`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSCodCom`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSBasITI`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSBasIT0`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSBasINI`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuTCo`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuSCP`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuSCH`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuSCE`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuSCD`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ATSAnuAut`** | `varchar(49)` | SI | Campo transaccional de Hosvital HIS |
