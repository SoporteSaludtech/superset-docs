# RCPCAJ1

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
| 🔑 | **`RcpFmPag2`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RcpVlr2`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpDocRef2`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpBan2`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpPost2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNroAut2`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNomAut2`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpCtaCte2`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpNoCnsg2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpUsTra`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpTurCod`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RcpAnCon2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
