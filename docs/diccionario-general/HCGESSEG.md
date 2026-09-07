# HCGESSEG

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
| 🔑 | **`HCGSCON`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCGSTIP`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGSFID`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGSFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGSDET`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGSFOL`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCGSUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
