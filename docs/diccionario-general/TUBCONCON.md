# TUBCONCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TubCedPac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubDocPac`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubFol`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubPPP`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TubFolCon`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubFecCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubNomCom`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubEdaCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubSexCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubRelCas`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubVIH`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubDNT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubEda`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubSinRes`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubBK1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubBK2`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubBK3`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubCul`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubBCG`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubPPD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubRX`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubPro`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubSR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubConUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TubConFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
