# MVTTERAS21

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvTerNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtTSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtNfac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtMaTpD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtTerPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDscEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTotDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtValAut`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtPorPar`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVlrAbo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVlrAut`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtParRec`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTCCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNotDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNroNot`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCscP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtPrCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNdoc`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVatP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCnpr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrAsEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrAsCd`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrAsUs`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrAsFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrAsVl`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrAsCd`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNoPag`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTrFcCxp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNDocCXP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTdocCXp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTFchFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTFchPrc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTCont`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCodHon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCodUVR`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTipTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtEstPrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTipPrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDesCar`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtOtrDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtIndGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtImpEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtEstAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtIndPrc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtFchPro`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTipPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtMpMeni`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNumAuE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtMSReso`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCanS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtFchSum`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCscS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNumDo`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTipDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtConIg`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtFueIn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVlrNeg`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDocNeg`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNroNeg`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtSedNeg`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtUsuNeg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtFchNeg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtMotNeg`** | `varchar(120)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0015`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
