# TMPFAC2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFCscS`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TFNitS`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BODEGA`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFcSu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFReso`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCanS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFValU`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVaTS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUSum`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFESum`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFSum`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFHSum`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TfUsuAnlS`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tfsnoma`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TfSNumA`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tfsctax`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSNDCT`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFcFchInv`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSTpoTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFPorImp`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`TfBodEnt`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TfNomg`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFvaTS1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFPorcPart`** | `decimal(13,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEstaAnu2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFchAnu2`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFOriSum`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoParS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEsPaXToS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFIFacSum`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCtvEntS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSCaue`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSPorIva`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSVlrSIv`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTIPLIQS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCOPAQT`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCOdAnuS`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCODIMPS`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFIMPSUM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFEtEnT`** | `numeric(1,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSCODHOM`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSCTEPAQ`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSCNSPAQ`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFRESOMET`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFSIDMIPR`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAnCaTr2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFReApTr2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAUTSUM`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
