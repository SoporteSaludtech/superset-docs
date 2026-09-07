# HCCOM7

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
| 🔑 | **`PPPCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPPHiCObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHiCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCtvIn7`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHiCUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHiDiPC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHiFeCi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHiCalA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPTipPac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPLocEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPLugExt`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPComTen`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPVIHAnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPPesIni`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPDiaCul`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPFecDia`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPTieSin`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPBac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPCul`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPHis`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPCuaCli`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPNexEpi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPRad`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPADA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPBK1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPBK2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPBK3`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPLugRem`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPCatTub`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPVIHAse`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPResTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPDesRes`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPFecEgr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPEgrObs`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPMDR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPPerSup`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPDirSup`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPBarSup`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPTelSup`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPTub`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPUMT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPFinCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
