# CTAPAG2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CxCPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CxCPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CxCReaSubN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaGru`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaIndR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaIni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaSdoI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaRes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaCxP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CxCReaSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
