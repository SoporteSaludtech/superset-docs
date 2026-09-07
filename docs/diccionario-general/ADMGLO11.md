# ADMGLO11

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AGlEmpCd`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlMcdpt`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlDocCd`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AGlRemNr`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AGlFacEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlNRdFac`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AglFRdFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlUsrRad`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlConDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlConNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGlConFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGLPERCER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGLFCHRAD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITABOEMP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGLFACDEV`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AGLANPCNS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0014`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGLNUMREC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
