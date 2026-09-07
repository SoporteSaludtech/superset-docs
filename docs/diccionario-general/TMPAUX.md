# TMPAUX

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TAEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TACntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TAuxAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TAuxMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TAuxNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TAuxDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TAuxCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TAuxSAnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TAuxSAct`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
