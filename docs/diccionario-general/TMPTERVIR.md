# TMPTERVIR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TmpEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpTerNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpTerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpNoFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCscP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTipDoc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpPrCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpNdoc`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpVlrTP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCntPrc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpVlrPar`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrAsCd`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCnsPrc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpFchFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpFchPrc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTerSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTerCCs`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCodHon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCodUVR`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTipTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpEstPrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpTipPrc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
