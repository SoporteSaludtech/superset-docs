# OPEBANCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MesMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AnioMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstPer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalMov`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fchCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`usuCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
