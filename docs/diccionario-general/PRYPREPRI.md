# PRYPREPRI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PryPtoAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PryPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PryCUOri`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrySUOri`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PryCCOri`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrySCOri`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PryPtoMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PryPtoVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
