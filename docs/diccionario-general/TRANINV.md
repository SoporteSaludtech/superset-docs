# TRANINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranCod`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TranDsc`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranTMvto`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranAMvto`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranExTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranDscEn`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranDscSa`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranSUnid`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranSValU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranAfeCst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCenCst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranSubCst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranDscAj`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranDctRef`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranAftPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnRepVal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCtaD`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCtaC`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranNatC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranNatD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranTIvCn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnCtrPre`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranNVLAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranTipo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnSalIn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnDonBon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntFarExt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
