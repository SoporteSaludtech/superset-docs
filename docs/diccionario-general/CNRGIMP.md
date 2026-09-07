# CNRGIMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CRITipOp`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCoCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CRIOpDs`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRIEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnRCXPMod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
