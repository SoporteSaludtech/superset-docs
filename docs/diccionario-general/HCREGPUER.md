# HCREGPUER

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
| 🔑 | **`HcPCtvPar`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HcPPuFchH`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcPPuPa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTAD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTAS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPPuls`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPTemCo`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPInvUt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPLoqui`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPConAn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcPMetAn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcRgtF051`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
