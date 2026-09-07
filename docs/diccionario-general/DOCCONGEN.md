# DOCCONGEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCtvGen`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConCodDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConFHoGen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConUsuGen`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocObsNGe`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCirCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCODI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONINFTEX`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONINFFIR`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONINFACO`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONINFFOL`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONINFIMA`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
