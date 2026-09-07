# EJEPREPRI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjePtoAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjePreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjeCUOri`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjeSUOri`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjeCCOri`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjeSCOri`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EjePtoMEs`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EjePtoVaP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EjePtoVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EjePryAcu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EjeEjeAcu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EjePtoEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EjeAcuEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
