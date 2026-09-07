# TRANSFE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TrsTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TrsLote`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrsSec`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsTran`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsDscTra`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsNumReg`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsSumDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsSumCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsBanco`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsCntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsCntVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsFchApl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrsForPag`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
