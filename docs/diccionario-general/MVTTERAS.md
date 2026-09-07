# MVTTERAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtTSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvTerNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtNfac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtMaTpD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtImpCod`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtImpPor`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtImpVrl`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
