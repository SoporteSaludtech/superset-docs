# RESULNOT

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
| 🔑 | **`RsNotCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AlumCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MECodE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipoA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipoB`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipoC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotObs`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotTpMd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotIdPac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotDoPac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsNotRegE`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsPonNot`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
