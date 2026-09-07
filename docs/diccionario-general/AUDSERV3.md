# AUDSERV3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutServ`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutCptEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServNit`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServAut`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServNro`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServExe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServDsc`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCtvAdm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNumFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipFac`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNumExt`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCodEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutOrdAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEspInt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCitEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCitSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCitNum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutVlrSol`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMsReso`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEstPer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutObsPer`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutUsuPer`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFecPer`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDiaPri`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Id`** | `numeric(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEnv`** | `numeric(1,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTFCHVII`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTFCHVIF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTPROLO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTORIGEN`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUTRUTCAN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
