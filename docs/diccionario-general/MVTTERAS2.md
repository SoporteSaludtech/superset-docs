# MVTTERAS2

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
| 🔑 | **`MvtAboCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtTipAbo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboCar`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboAut`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboDE`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtAboFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAboDcCxP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAboNoCxP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAImpGen`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAboDPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAboNoPag`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAVlrEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAImpEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPeaEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MADocRC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MANroRC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MASedRC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
