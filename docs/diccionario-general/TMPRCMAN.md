# TMPRCMAN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TRCEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCNroDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCCliCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCstvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCSedFac`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCNoFac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCConCnt`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TRCDocFac`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TRCModo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCSaldo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCVlrPag`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCMMENI`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCCUtil`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCSCUti`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCFchVen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCFchPag`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRCPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
