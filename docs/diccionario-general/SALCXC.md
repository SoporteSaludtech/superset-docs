# SALCXC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SCANIO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SCMES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HojNumObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SCFCHOBL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCVLROBL`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCTOTCRE`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCTOTDEB`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCNRORAD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFCHRAD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCTIPGLO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCSTAGLO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFCHRCG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFCHRDG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFCHCAN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCVLRGLO`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCINDDEV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCNRORG`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCCLADOC`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCNROCAS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCINDFAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCHOJPRF`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFCHRR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCNRORR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCPLZ`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFVFO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCFVFR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCDVFO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCDVFR`** | `int` | SI | Campo transaccional de Hosvital HIS |
