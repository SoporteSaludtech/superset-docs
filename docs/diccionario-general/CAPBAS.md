# CAPBAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPNom1`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNom2`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPApe1`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPApe2`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFchN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPSexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDire`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTele`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodB`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPEstC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPGrEs`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MOCodPri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNHiC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPUCod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNOMC`** | `char(243)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mpfalta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTmpRes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTTmRes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPstNuc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPIndJfF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNivEdu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPIngMen`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDocInt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpLgExp`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpTele1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpTele2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpMail`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodBE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNumHCIn`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNivEEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPOtrAfl`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpCtvoActe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpCtvoAtn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpCtvGes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpUltCtPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpUsrPrf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPEmpTra`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPOtTiAf`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPacNN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCtvMed`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPSemCSis`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPSmCtCm`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPIpsAtn`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTipAfi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCalAfi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdCodMNac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdCodDNac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPEstPac`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPDere`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPBECar`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPBEIps`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCodPai`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCodDisc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCodEtn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFchDef`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCPEtn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDocMa`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCedMa`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCscInM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPConNac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPGrPo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPViveS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpVivEcon`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpOcuAnte`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpProTot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFOTPAC`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODSEGCA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODCAT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODSEGTR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODTRA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPINDDER`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPINDIZQ`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCARNET`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPFECACT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPSbGrPo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPIndEtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPConPob`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPEREXPU`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPAPTIT`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPAMTIT`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNOMTIT`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPPARTIT`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPINDEC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPINDIS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCEDTIT`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPInscMFA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODMAFI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCODDAFI`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDIRECOM`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PUEID`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TIPBONID`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MpATrEd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNomSoc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SeDoIdCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPOBSPAD`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNOMPAD`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDOCPAD`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCEDPAD`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNOMMAD`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDIRCOD`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDIRREF`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPDIRSEC`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPZonRes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
