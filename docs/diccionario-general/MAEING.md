# MAEING

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MIFchAdm`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MATipDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MiDMCodi`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MiCntHsp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MIExtEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MIEstSld`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MInUsrReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodIPS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFchEgr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodDxS`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EpiUltCtvo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
