# PQUEUE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PQID`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQEMP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQNAME`** | `varchar(128)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSTARTDT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQENDDT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSTATUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQINFO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQNOTIFY`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQUSERID`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQWRKST`** | `varchar(128)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQMESSAGE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCLASS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
