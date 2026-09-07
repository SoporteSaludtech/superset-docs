# BLTAINV31

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltUbiEst`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltUbiDIz`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltUbiNiv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltUbiZon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BltUbiCan`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
