# CAUINGPRD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPCodCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPTipReg`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPCtvPS`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPAnioPr`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CIPMesPro`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CIPCodPS`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPMPNit`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPTipPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPNroFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPMatipD`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPMaClas`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPFchFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPCantid`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPVlrUni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPVlrTot`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CauIPCie`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPFchSys`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPUsuPro`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPBodEnt`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPUVRCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPHonCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIPIndCrz`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
