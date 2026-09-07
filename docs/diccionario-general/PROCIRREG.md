# PROCIRREG

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
| 🔑 | **`PROREGCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PROREGUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROREGEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROREGFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROREGMOT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROREGOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
