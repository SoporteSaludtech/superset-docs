# REIINTER1

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
| 🔑 | **`MECodE`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMCodi`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIDgItTp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDgItCl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDgItOb`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInt1Pa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
