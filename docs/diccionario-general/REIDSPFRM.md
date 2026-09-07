# REIDSPFRM

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
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIDSCnDs`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSCnSo`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSmEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSmFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSUsRe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSCnDe`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSCntD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSUlCn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSCtvI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSTiDe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSTiOr`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICnsPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICnsSui`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICntUsa`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSPsEr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISpsCnf`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISpsEc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodPaq`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDInUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINroSol`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSmPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDSFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
