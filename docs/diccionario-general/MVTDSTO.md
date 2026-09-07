# MVTDSTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtDCn`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TerCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipDesCd`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDsVl`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDsNc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstFh`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDsSd`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDscUC`** | `int` | SI | Campo transaccional de Hosvital HIS |
