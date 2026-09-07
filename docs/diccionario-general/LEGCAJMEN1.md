# LEGCAJMEN1

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
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegRef1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegRef2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCon`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DtLgVBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegCP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegSR1`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETPRFEQU`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETNUMEQU`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETDOCEQU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETSEDEQU`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DetLegRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGVI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGCI`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGGD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGIT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGFA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DETLEGNA`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
