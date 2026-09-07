# SOLCOTREQ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`SolCotRId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SolNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SolItm`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`SolSedReq`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolDocReq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolNroReq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
