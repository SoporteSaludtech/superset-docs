# ORDPAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OrdPgNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgBen`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BANCOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCpt`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgTrn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVAut`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgDcAt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgNrAt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgDPg`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgNPg`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgChq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgChe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFDs`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFPg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUPg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFSys`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVNeg`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUMA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFMA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgUAA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFAA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
