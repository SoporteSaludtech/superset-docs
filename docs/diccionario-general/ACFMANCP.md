# ACFMANCP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFMCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFMPNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFMPEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFchC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPUsuC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFchP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPUsuP`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFchS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPUsuS`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFchE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPUsuE`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPUsuA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPObsP`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPObsS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPObsE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPObsA`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMPHer`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
