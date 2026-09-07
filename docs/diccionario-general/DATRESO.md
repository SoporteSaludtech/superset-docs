# DATRESO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`codResol`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`codIndicad`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DatResVlr`** | `varchar(8000)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DatResFch`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`DatResObs`** | `varchar(8000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatResImp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatResHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
