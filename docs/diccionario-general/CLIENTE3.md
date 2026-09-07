# CLIENTE3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CliDscCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CliDiaIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliDiaFin`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliDsc`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
