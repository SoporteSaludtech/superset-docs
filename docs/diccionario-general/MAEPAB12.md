# MAEPAB12

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNumC`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCODTURN`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCSCTRN`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MMFECIASG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECFASG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMOBSRASG`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODAUX`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
