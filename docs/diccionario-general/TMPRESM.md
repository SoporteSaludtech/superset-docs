# TMPRESM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSedCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpCntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpCUti`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSCU`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpCCos`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSCC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpTerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpSalAnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpSalAct`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpResDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpResCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
