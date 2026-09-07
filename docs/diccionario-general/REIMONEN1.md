# REIMONEN1

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
| 🔑 | **`REIMonFeHo`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItmCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIMonIVlr`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMonPa1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReiItCnLi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReiItAbLi`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
