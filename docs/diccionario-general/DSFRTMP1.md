# DSFRTMP1

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
| 🔑 | **`DSmCons`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DSmFloCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmFloSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmFloFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmFloCntD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmCnsMov`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
