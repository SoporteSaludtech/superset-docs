# PARMPPTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmPtoCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrmPtoDsc`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParGir`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDSCdp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDRadFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDOrdGir`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDObl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDIng`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDIngRco`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDCom`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDCdp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAObl`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAnuOrd`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDAnuGir`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParAprPpto`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParAOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParACom`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParACdp`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocAIP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocMPG`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocMPI`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDocARV`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmPtoF1`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmPtoF2`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCgo1`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCgo2`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDoc1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDoc2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmPtoF3`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmPtoF4`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCgo3`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCgo4`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDoc3`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDoc4`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFirCer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmNCGRe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmImpNV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFirExc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmGirObl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFirMP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParCanDec`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
