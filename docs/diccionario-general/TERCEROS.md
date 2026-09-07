# TERCEROS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TrcCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrcTpoIde`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcRazSoc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcDir`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcTlf`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcFax`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcAAe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcEmail`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcMDCodD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcMDCodM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcMDCodB`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCoCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcTipEnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcNit`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcDigVer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcSgl`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcTipTrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcRsl`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcReiCRp`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcReiNRp`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcRepLeg`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcPrmNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcSegNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcPrmApe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcSegApe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcExcMM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcMnjRUT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaisCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcUsuIna`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcFchIna`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcNoDom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcAplIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcIdeERP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCFECNAC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCSEX`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCANLCOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcIndARe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCCLC1`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcResFis`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcRegFis`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcResTri`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcParRel`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcEmaNCP`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCodChi`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcClaDoc`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcRazSoT`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
