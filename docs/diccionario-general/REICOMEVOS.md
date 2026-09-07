# REICOMEVOS

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
| 🔑 | **`REICnSoAp`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIFeSoAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHoSoAp`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMeSoAp`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEvoPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEvFoHc`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
