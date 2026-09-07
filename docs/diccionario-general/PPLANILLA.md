# PPLANILLA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PPEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPlaCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPMENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPClaAte`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPFec`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotP`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotS`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotF`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotSI`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotAB`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPIdPrcCo`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPUsuGen`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPTotImp`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPNumRad`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPUsuRad`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPFecRad`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPEstRad`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPEstado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPEstCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PNroNotNC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PEMPCODNC`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PMCDptoNC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PDocCodNC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
