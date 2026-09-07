# HOJAGASTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HisHojCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HisHGCtvI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisHojCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisHojObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisHojFHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisUsuHoj`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFolHoj`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
