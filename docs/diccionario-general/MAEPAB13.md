# MAEPAB13

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MACODTAR`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCSCTAR`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MMFECASI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMOBSPRE`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMOBSFIN`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECFINT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECINCT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
