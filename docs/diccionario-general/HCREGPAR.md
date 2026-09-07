# HCREGPAR

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
| 🔑 | **`HcPCtvPar`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcPPosPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPParPar`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPMemPar`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPRotMem`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPRotFeH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPMeconi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPIndCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPAntibi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPAnalg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTrans`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPManAc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPCtvGe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPCorAn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPSeICA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcRecPor`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNAcomp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNPres`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNPlacen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNDesgar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNTermin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNLigCor`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcNEpisi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcIniAte`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNCtvNa`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCAUMUE`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPUEMED`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPUEINM`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPEREXP`** | `varchar(2500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCmpPrt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcUtrInbr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
