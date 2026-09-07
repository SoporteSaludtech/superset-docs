# PARMCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmCon`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrmConDsc`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParmAjuInf`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDACH`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmFirm1`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmFirm2`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmFirm3`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmFirm4`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCgo1`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCgo2`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCgo3`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCgo4`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDoc1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDoc2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDoc3`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDoc4`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocCie`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParCntInv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocDep`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocMAc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDCieA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCajMen`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDetRec`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocLeg`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocAmr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocMDf`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDNCCmp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParModNit`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocPla`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParModFApl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParAdiAct`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDCieBl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAnuRC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocND`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDCauPr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAnuPr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAcTDp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocNmk`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocSSk`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocPFk`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocPvk`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocTop`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDOrdPg`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAutOP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDDifCm`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocRad`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDTraAcF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParAuActF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDBAcF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDDifDF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAval`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDCnAcF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDiDeFC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocSin`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParPrgPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFrmMC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMTRSNI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParAnoUni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
