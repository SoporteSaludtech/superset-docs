# HCREGDPA

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
| 🔑 | **`HcPFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcPDilPar`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPPosMat`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTenArS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTenArD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPPulMat`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPFreCFe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPDurCon`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPFreCon`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPDolLoc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPDolInt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPAltPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPVarPos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPPrBor`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRDAmeno`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`HcPCtvGm`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`cHcPMeconi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cHcPRotMem`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cHcMemPar`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPFOLREG`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRDPAFCF`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
