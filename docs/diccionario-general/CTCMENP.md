# CTCMENP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CTNumID`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTipID`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTDiag1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTDiag2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTDiag3`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTipTra`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTEnfACo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTReaPOS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTConPOS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTUlCtvD`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTMsCoNP`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPriAcN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPosN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPreMeN`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTDosDiN`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCanNPO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTieDuN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCncCN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTiTrDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCFeHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCodProN`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTipReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCEstAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTAltPos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTMej`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTUniSuc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTObj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTmpRes`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTRieViSa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTAutMeIn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPosTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCEscTmp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCCodCum`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcForCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndApr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndUnr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfHrO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfVIH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndCnc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcMotErC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcDsnPrt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndHue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcCodOdx`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcindEvC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcPrcDes`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndRcr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcCodUti`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTcFrcUso`** | `numeric(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTcTmpUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfSel`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnVIH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnCnc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcMedExi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndRst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndAdv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcDesIns`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcDesSum`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcPrvInt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndCid`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndPBS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndEvd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcMedDex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfErc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfPrt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcEnfHIV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCENFCCP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcHosDom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtcIndEsp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
