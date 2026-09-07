# HISBIOPSD

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
| 🔑 | **`HISTRIM`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCODRIEG`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCONRIE`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISDESRIE`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDESCONR`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCALRIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
