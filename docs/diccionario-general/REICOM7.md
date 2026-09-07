# REICOM7

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPPPCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIPPPDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiCObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHCtvI7`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiCUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiDiPc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiFeCi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHiCalA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITipPac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILocEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILugExt`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REiComtem`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIVIHAnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPesIni`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDiaCul`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecDia`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITieSin`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIBac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICul`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHis`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuaCli`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINexEpi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRad`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPADA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPBK1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPBK2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPBK3`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILugRem`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICatTub`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIVIHAse`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDesRes`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecEgr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEgrObs`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPMDR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPeSup`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDirSup`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIBarSup`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITelSup`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPTub`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPPPUMT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICOMPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICOFoHc`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
