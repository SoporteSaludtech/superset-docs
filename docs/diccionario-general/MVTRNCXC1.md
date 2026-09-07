# MVTRNCXC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvTrnNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvTrnCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvTSedTrn`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTCodTrn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTCUTrn`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTSCUTrn`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTCCTrn`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTSCCTrn`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTTrcTrn`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTDrfTrn`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtNatTrn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVlrTrn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtVBsTrn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCntTrn`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrnTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtCntVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTDocFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
