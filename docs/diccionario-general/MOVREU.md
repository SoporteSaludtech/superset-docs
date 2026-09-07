# MOVREU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodReuCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MRCntEnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MRCntReu`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MRCntDsp`** | `money` | SI | Campo transaccional de Hosvital HIS |
