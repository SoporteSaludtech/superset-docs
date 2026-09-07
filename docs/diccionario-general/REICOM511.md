# REICOM511

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
| 🔑 | **`REIPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMCodi`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIDgRsTp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDgRsCl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDgRsOb`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICOM11P`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
