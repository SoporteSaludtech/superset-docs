# DESFINPRV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOPNoObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DesDiaIni`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`DesDiaFin`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesTaz`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesValPry`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesValEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
