# REILIQUID

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
| 🔑 | **`REILqCstv`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REILiqDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqCnFr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqUnCd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqVia`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqFr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqObs`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqUsFo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqEdo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqHoIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqInCP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqMsCo`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqMsPr`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqMsFo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqCnCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILiqPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILqCsHC`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REILQTPPR`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
