# LOGRMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogRmpAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogRmpMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogRmpId`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`LogRmpTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogRmpUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogRmpFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogRCuIni`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogRCuFin`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
