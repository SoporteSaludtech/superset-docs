# ESCPARRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTIPDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ESCCODRES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ESCDETRES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ESCINDRES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ESCPUNINR`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCRESTXT`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCREGDESD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESRINDIMG`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCIMGNOM`** | `char(256)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESCIMGEXT`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
