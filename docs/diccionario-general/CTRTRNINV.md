# CTRTRNINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTIApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTIAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTIMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTITBg`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTITrn`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTIGrp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CtrTICDeb`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrTICCre`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrTINC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrTIND`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
