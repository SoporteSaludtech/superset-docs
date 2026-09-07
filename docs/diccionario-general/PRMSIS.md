# PRMSIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmCodSis`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrmDscSis`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmMnjCUt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDgCU`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDgSC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmMnjCCo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmVlCtCC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDecIva`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmMonCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmConInv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmFluCaj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTipPre`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCxCPE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmAjsInf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmCtaCst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmMovBaj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmIntGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmDesFin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmAdmCen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmSedAdm`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCnsImp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCntInv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCntAEnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTrasAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCieAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmAnuFNC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmMetCIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmUsaMAg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmSlInUb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmSlUbAu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParmActPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmUsCenC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTCIng`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDigPla`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCsnPla`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmImpTex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmTrnSTr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmRevIng`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmGloFRd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmDepFis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmModFch`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCnFRd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmModFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmMFI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmEmpCnv`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCntSed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmNomTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmModFeR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrmCntGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMDCTU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMDCTF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMDCTC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRMVALPRC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
