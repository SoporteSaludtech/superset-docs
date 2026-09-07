# BLTAINV2

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
| 🔑 | **`BltNroCnt`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BltEstCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltUsuCnt`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltFchCnt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
