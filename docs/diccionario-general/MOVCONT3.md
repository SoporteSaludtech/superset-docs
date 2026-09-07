# MOVCONT3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvCCpt`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCCdg`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCMonBse`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCTasCmb`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCUsuAct`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFchAct`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCUltCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCmpAjs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvFchSys`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCIdeTrb`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocRet`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroRet`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroAut`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFchEmi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFchAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvSRCCm`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvSRCErr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCMayAux`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCMayGen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCnvMon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCOrigen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCNumEqu`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvcEstPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCDOCEQU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCSEDEQU`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCFORPAG`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdPrc0001`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCEREMA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCERMAN`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCPUNEMI`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCCodMPD`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCTipCom`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroANC`** | `varchar(49)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroNC`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroACM`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCTipLC`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCSedLC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCDocLC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroLC`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNroALC`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCFchALC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCPunELC`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
