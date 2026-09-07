# CASOS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CSCons`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CSFol`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CSMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSEspMed`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsFolRel`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsFecRel`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsAtnFol`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSCtvoIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSClapro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSFecAdm`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSUsuDes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSFecDes`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
