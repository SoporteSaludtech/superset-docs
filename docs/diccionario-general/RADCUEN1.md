# RADCUEN1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadRegCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RadCodCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCodCon1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadDocCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadSedOrd`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadNroOrd`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadValAnI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadValIva`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadValNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadNumFac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadObsFac`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUsuDoc`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFchDoc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCnsUlt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEstFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadSeFCCo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCoFCli`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFchFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueDoF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueCnF`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadRegCnF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadNumRem`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFchRem`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUbiFac`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUsFa`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadInDe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEstEnv`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaPuRuCF`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEstGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadAgruCo`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadTipOpC`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCntCoC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1CT`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AF`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1US`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AD`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AC`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AP`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AH`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AU`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AN`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AM`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1AT`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmCT`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAF`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmUS`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAD`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAC`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAP`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAH`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAU`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAN`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAM`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1NmAT`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExCT`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExUS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAH`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAN`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAM`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1ExAT`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Rad1RiVa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElCT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ra1ElAT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFeSerI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFeSerF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCiuCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadDepCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCenCuC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
