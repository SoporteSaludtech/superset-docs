# HCCUIEN

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
| 🔑 | **`RgECodTrn`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RgENutMet`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResCan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResCaL`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResVen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResVeP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEResTrq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgETpoSnd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECarCAV`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECarCIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECarCIO`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECarFiA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECarFAM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDSnD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDSnV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDTbT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDCis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDOst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEElDTMT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuEBaG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuEHiO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuEZoP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuELoE`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuEPiD`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuETra`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuETrD`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuELub`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuEMas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECuECaP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEAltSVt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEAltAct`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECNCSue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECNVFml`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECMSCmF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECMTNut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRTOrt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRTTCm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRVent`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRPNeu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRVCor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRPeep`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECRFIO2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCAVcm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCCmCV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCCmCm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCSwGa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCMahk`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCNHem`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCMpso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCOutP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCMFrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCSens`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECCAlMo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECETTcm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECETMCm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEFchITr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgELinArt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgELinArC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEHemoba`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgEHemSit`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgESoVeEx`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgESonPen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RgECatPer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
