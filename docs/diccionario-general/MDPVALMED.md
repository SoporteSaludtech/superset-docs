# MDPVALMED

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpMedNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpMedOxi`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedEsp`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPsi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPdi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedTar`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedFca`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPrp`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPes`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPre`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedAca`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpCodDpt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`McDptoDpt`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRufCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpMedFle`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedFab`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedFlu`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPag`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedPat`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedMed`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedQui`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpMedTox`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
