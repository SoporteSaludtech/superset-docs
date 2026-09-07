# RIASRUT

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
|  | **`RIADes`** | `char(180)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIATipRut`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIADurMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIASAyuRap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEdaIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEdaInEn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEdFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEdFiEn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIASexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIACNCCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIATipPro`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAITBC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAVIH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIANoRep`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAInterv`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEntHog`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEntEdu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEntLab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEntIns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEntCom`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAPyPCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAActiva`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
