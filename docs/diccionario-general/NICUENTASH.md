# NICUENTASH

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NICNTCOD`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NICNTPRC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NICNTACT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
