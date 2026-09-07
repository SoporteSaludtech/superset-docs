# PLAEJETR2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleCnsPtR`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleCnsCoR`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PleCnsAcR`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PleCnsAct`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCodPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleEspMed`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCitNum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleTieCit`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleNumFa`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleDocFa`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsFa`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PleCnsCot`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
