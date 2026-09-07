# MOVACTFIJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovActNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TraAFVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TraAFCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovActFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovEstCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovUsuCod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovNroCmp`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovConTras`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvActVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovUsuAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovFchAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovAcFAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
