# LIQUIDOS

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
| 🔑 | **`LiqCstvo`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LiqMscodi`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqMsPrac`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqMsForm`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqCncCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqDsc`** | `char(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqCntFrm`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqUndCd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqVia`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqHorIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqUsuFor`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqEdo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqInCaPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqEstFol`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LIQTIPPRO`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
