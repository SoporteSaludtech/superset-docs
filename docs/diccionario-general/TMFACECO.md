# TMFACECO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TMFUsu`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMFCenCo`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMFTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMFPrCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMFSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TMFCant`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TMFVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
