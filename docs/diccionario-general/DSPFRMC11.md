# DSPFRMC11

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
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSmTpoTrn`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSmCnsMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSmCnsLot`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DsmCodLot`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmCodPrv`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmFchLot`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmCntLot`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsmMvtLot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
