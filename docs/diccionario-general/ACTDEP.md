# ACTDEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DepAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DepPer`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DepCtoHis`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHisAcuAnt`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepMes`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DHisAcuAct`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepCont`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
