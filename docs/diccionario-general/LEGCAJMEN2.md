# LEGCAJMEN2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LegCMNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DetLegIte`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DetLegCL`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DetLegCPN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCPD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCDN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCDD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegVL`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegTCL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCCL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegTL`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegEL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegUL`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegFL`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegR1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegR1S`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGCI`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGGD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGIT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGFA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGNA`** | `char(49)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGVI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegPDS`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegNDS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegDDS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegSDS`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegTC`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegTPR`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegPI`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegPEL`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
