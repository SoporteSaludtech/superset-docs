# MAEPAB3

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
| 🔑 | **`MMCODCSC`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MMESTTAR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMUSUASG`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECASG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMNOTPRV`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECNTP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MNNOTDEF`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECNTD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
