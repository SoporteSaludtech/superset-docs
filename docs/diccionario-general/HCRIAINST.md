# HCRIAINST

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
| 🔑 | **`HRIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAInsCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RIAInsCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RiaInsDet`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAISex`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAInTAc`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIEst`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFAs`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFAp`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFOr`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFcAs`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFcOr`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIFcAp`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIEsAs`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIEsOr`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIEsAp`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIAtAs`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIAtOr`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIAtAp`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRIAIRes`** | `varchar(128)` | NO | Campo transaccional de Hosvital HIS |
