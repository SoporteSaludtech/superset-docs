# INGRESON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`InNCtvNa`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`InNFchN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPeso`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTall`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPece`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPeto`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNApg1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNApg5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNCaMu`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDiaRn`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDiaRN1`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDiaRN2`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNUNac`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNHorM`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNFcMu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNRegNav`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTaFeAc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPres`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNMomMte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTermin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPlacen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLigCor`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDesgar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNAcomp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTAcom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNEpisi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNReEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNReAsp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNReMas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InnReMsj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNReOx`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNReTu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNFaSP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDefCon`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDefCMy`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLacPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNVitaK`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNProfOc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTipRN`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNEstRN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNNomRN`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNRefer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNCtvGe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNFcHrEg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNMotS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNIPSRem`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNAlAl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPesEg`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPosEg`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNVDRL`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTSH`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNHbPa`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNBilir`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTxoI`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNMedR`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNMedE`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNOrdNac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLabor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNExp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLAmn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLAC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNLAO`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTPH`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNSuFe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNObs`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNSeGe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNAbo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNF1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNF5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNF10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNF15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNE1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNE5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNE10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNE15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNT1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNT5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNT10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNT15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNI1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNI5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNI10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNI15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNC1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNC5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNC10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNC15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNSuc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTol`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNOri`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPEH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNNL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNDep`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNPO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTROP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNTiPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNBCG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNCodOp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNObCop`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNAPG15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNAPG10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNVacHepB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNVacBCG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNPRNOMB`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNSGNOMB`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNPRAPEL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNSGAPEL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INNOBSDEF`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InTmzAud`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InTmzViz`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNF20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNE20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNT20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngMdcInt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNC20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngBlsInt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDscEgr`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngDgnSld`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngPlnTra`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngHrsHdr`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngLiqAmn`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INPRIPER`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INDATREC`** | `varchar(900)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INMEDANT`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INSIGVIT`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INADANEO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INPUNSIL`** | `varchar(1500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INAPGARUN`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INAPGARCI`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INAPGARDI`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INAPGARQU`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INACTNEO`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INOTREXA`** | `varchar(450)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INEXAFIS`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INACTVEI`** | `varchar(2000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INDIAG`** | `varchar(900)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INDCOMP`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INCAUMUE`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INOTROS`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InnPrt051`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InNI20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`INSEGPER`** | `varchar(2600)` | SI | Campo transaccional de Hosvital HIS |
