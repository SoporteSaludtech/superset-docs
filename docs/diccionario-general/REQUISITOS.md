# REQUISITOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`RCCdgRqs`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RCDscRqs`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCRutIma`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCImaPer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCStsRqs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCTipReq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCClaReq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
