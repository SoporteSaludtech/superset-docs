# REIHOJGAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIHojCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIHGCtvI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHojCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHojObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHojFHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHojPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHojPFo`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
