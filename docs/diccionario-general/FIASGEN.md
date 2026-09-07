# FIASGEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`FEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FSEDE`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FFIAS`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FFOLIO`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FCONTRATO`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FDOC`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FTIPDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FDepart`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FMunicip`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FFecha`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`FJson`** | `char(512)` | NO | Campo transaccional de Hosvital HIS |
