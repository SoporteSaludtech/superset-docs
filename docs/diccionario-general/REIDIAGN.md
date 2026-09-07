# REIDIAGN

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
| 🔑 | **`REIDXCOD`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICNSDX`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDXCLS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDXTIP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDXObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstHCD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDxFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDXInfN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDMOtrCo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDMCodA`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDXApto`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDTieEv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDPreNo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodMIn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodBIn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodDIn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodPIn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConSin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFchInv`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFchInS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFchCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAPEDTG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAPEDTD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
