# COMMOCIR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ComCoCr`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ComCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ComCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComCodMe`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComFeHr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComMcDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ComEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
