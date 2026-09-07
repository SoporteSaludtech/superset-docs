# PRGORDPAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgOrdNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrgFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgFchPro`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgCodBan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCTESCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODTRN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCVigTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgConce`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgEstAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
