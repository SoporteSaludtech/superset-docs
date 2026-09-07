# BODDAT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`BodTipIde`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodIdePac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodConIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodAct`** | `char(11)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodAmbPre`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodNumDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BodFecNac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodSexPac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCodDep`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCodMun`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDiaPri`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDiaTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDPEgr`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDREgr1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodEstSal`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodFecSer`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodForRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDiaEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodValAct`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodVAUsu`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodNit`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipAte`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipSer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipTra`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodMunAte`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodSed`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodIpsAte`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodIdeHis`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodSemAfi`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodFSSer`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCauExt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodFinSer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodNomPab`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodNomCon`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodEstOrd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodNFact`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTipDoF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodClsDoF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
