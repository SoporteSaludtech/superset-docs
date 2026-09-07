# MAEINGLEVE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MIFchAdm`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SlAFchHra`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`SlANomInf`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlAObs`** | `char(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlATpoAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlATmpAut`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlATpTmAu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlAAtc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlANroAut`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SlAUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
