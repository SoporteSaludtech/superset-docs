# MDPDATDEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MdpDatCon`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`EmpCodDpt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`McDptoDpt`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpDpoCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpDepTpa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
