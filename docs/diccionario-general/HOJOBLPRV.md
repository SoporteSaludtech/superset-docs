# HOJOBLPRV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOPNoObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPFchObl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPFchRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPTpPz`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPVlrCuo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPCuoIni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPVlrObl`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPVlrMEx`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPTotCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPTotDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPMvTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojFchCan`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPEstAfPt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojNroOC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojBasDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojDocOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPSedCau`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPDocCau`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPNroCau`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPHom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HojSedOc`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPCodCon`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPCodCoR`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOPFchVen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
