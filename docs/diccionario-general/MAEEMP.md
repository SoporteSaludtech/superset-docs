# MAEEMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MENOMB`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEcntr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeIndForPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTieForP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTieAnFP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTieDeFP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`METieModF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEestado`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEEmpcod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEPasc`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MePasd`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmPasp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MePasp`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmPas`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEdiAv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCtOrd1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmCtOr1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCtOrd2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmCtOr2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCtRes1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmCtRe1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCtRes2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmCtRe2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCtDfC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeEmCtDfc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECopa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECoInf`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEComo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEPOsx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECApi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEPARt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEATope`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MESITRIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEFACTUR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDiaGls`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDiaRGl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtoIndGoC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDspMed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEUltCta`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MERdCxGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEobser`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCodRip`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAprRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeInFaNo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCoFaAgr`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeFacFos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeIndCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAutOrd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAutAno`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCarAdm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAplMul`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeGExcCP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MePrcSub`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEEps`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEAprRed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCarApRe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTipAprR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTipTrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeDirRad`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeConRad`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAleRad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCodPFa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeAutMed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeIntLAm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeDisIva`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeDiaAsC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeIncIva`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCamSer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCitMed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeLiqTeCM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCntrST`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEASEG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeDesAnx2`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeDesAnx3`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MELIQEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTrnSis`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECONRIP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEFACFIN`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEFACCAE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEFACDX`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEPYPCOMO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEPLACOD`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEMOCOD`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAINDFIAS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`METRNSID`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDPAFAC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDARESG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDRESGL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDRECGL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDIAARD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MERESDEV`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MERECDEV`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDIAARF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDIARAD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECONDEF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEORDPOS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`METipOpeF`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`METECSAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEHOMSER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MePrAdAt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MESIFFA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
