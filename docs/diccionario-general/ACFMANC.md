# ACFMANC

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
|  | **`AcFMVig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMCon`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMTer`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMMNro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMInt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMUsuA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMUsuIn`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMUsuT`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMUsuN`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMUsuC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMFchC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMHer`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMAPri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFMCnsP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
