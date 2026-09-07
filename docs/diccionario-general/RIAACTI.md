# RIAACTI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIACodAct`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAActCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAFreAct`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIASexPob`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIATipPrf`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIATipAct`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIATieAc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAActPre`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIACodAPr`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIASecAct`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIARemAct`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAReqAgn`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAAgnAct`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIACitCon`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIATiPrfO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAFicCtr`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAEstAct`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAACTOPC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIADiasAct`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAActFin`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RiaFinDese`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
