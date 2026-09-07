# BANMOV

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
| 🔑 | **`BanMvNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BanMvTrVi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BanMvFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvCBan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvPrc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvTrn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvCnp`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvMBse`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvTCmb`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanMvEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanDocRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
