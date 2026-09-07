# MONENF1

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
| 🔑 | **`MonFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItmCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MonItmVlr`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItCnLi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItAbLi`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
