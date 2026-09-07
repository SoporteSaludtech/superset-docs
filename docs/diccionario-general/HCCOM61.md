# HCCOM61

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PntCodi`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AntObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntObsFlu`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RNQCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntPar`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntIndPat`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntMen`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntRUR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntRCA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntRDu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCRUC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDRUC`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNPar`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNCes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNAbo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNMol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNEct`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNHij`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntEGe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFPP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntPla`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCMP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDMP`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntUEP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNHV`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNHM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNHMEPS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNHMDPS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Ant3AbC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntPUP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCMPF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDMPF`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntTotGP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntGem`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFMP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntNroCS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntAES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntAESC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntAESO`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFlu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUBx`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCUBX`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDUBX`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUMa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCUMa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDUMa`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFUCo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCUCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDUCo`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTEPSRN`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntViaPrt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntTmpPrt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmAbr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmRPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmPlm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmLgm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmRCU`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmAbt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmOtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntRtnPlc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntInfPrt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntHrgObt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntPrcl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntEclm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntSndHep`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmpOtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmCal`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntCmpCl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTTERHOR`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTEDAIVS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTEDAMEN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OtrObsAnt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntFrm051`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
