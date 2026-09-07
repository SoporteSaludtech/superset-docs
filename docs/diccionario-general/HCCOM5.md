# HCCOM5

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
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCPrcTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrStGr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCPCan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCpObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrAutNom`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrAutNro`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OPrIndUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCtvIn5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCtvEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCscCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrcUsCa`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrcFHCa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCarIntL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDosCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDosLot`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDiaPT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCalMue`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCResNPr`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMINPRES`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMINUSER`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMINFECH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRORIOR`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRORIKY`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCORPRCIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODPET`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFECPETI`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCQUELAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDOSQUE`** | `char(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFREQUE`** | `char(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFECQUE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFOLQUE`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUSUQUE`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRUTCAN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCANRES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAgVOjIzq`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAgVOjDer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPacCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCSedaci`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCBioMolG`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCProObM`** | `char(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDesMac`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIndMat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCANPOS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
