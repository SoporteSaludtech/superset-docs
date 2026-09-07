# REPATS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RATAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RATMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RATNumEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATTotVen`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATCodOpe`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RATFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
