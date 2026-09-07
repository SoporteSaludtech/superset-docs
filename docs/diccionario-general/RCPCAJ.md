# RCPCAJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcpCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`RcpFmPag1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpVlr1`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpBan1`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpDocRef1`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpPost1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNroAut1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNomAut1`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RCpObs`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpCtaCte1`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpHor`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpHorAnu`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpUsrAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpTur`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpIndAD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNoCnsg1`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpAnCon1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
