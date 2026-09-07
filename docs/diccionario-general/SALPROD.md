# SALPROD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SldAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SldMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SldCstPrm`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SldUni`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SldVlr`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SldEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SLDCSTPRN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
