# PPTOREC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`SalPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalReaIni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaSubN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaGru`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaIndR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaRed`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaAdi`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaSdoI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaRes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaCxP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalCdpExp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalCdpxEj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRgpExp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRgpxEj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRopExp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRopxEj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRGiExp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalRgixEj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalReaSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
