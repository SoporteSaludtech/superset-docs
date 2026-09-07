# PROCIR3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SumCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CntSum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SumPr_Ps`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SumEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
