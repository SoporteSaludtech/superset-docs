# CASCAR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CasCarDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CsCrNDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CsCrCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CsCrMeNit`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrVlrImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrCuen`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrClien`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrSelCas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrSelPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrEstItm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CasCarVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrTerAsi`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrCpPrc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrPropio`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrCnsSP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrCodSP`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrMTpD`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrNFac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrSFac`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrDsto`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrDFac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CsCrVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
