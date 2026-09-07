# HCCOM33

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
| 🔑 | **`EVONum`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EVOULIN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVOFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVOHOR`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVODES`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVOMED`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVOEpc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EvoIndMoE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVOCODTRA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEVID`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEVCOB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCEVPRC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
