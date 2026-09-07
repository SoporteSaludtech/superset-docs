# DETCUOPAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CuoDetId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PagAcuId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PagNumPag`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DetValAbo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetEmpAbo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetSedAbo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetDocAbo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetNumAbo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagEMPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagMCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoAPagId`** | `decimal(4,0)` | SI | Campo transaccional de Hosvital HIS |
