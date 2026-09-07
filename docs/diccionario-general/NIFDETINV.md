# NIFDETINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NIDEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDMSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDTIPPRO`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDPER`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDMES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDBODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIDPEV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCEV`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCOSPR`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCOSPRN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDDETINV`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDDOCCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDDOCNRO`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDFECPRO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDUSUPRO`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDSALDO`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCTADEB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCTACRE`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDGRPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDTOTREV`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDSALRV`** | `money` | SI | Campo transaccional de Hosvital HIS |
