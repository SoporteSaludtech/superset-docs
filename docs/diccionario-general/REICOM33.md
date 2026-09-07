# REICOM33

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
| 🔑 | **`REINUM`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIULIN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHOR`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDES`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMED`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEpc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIndMoE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREPa33`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoHC33`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
