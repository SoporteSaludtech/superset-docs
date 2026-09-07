# ORDPAG1

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
| 🔑 | **`OrdPgCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`OrdPgSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgTer`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgObl`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCVi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCta`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgSCU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgSCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFlj`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCpFj`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgTra`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgBan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgPrcD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVDs`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgDEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVlOr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVlAu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgPrTe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgCntA`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgVrEx`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgFRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgTpPz`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgNrOC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgDOCo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgMvTr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgEAfP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgSeOC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgSede`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgOrdNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgAN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdPgAD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
