# INTERCN

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
| 🔑 | **`MECodE`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IntEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntFchRsl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntObsOrd`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntDscRsl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntUsrRsp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntNumAuE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntReqAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntNroAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntNomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCtvEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntUsrCan`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntFchCan`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntOrdAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntAuto`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntDiaPT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCitAsi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntObsCan`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntMoCnTp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INTOBSREC`** | `varchar(6000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INTFOLHIS`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCnlCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IntCnlTpo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`INTMOTINT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
