# MOVINVCUE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MovEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovAnio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovTip`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovTran`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovGru`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovBodTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovBod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovEoS`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MovCtaDeb`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCtaCre`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVlrEnt`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVlrSal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCanEnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCanSal`** | `money` | SI | Campo transaccional de Hosvital HIS |
