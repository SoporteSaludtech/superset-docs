# MDPVALANT

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
| 🔑 | **`MdpAntNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpAntPes`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntTal`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntImc`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpCodDpt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`McDptoDpt`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpNutCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpAntCin`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntCad`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntRel`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpRieCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpAntTri`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntSes`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntSup`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntAbd`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntPgr`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpGraCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpAntBic`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntSep`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntMfo`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntPan`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntBre`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntBfe`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntHum`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpAntFem`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpClaCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpAntObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
