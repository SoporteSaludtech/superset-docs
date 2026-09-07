# SR_TechnicalAnnex02

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ClientType`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CompensationType`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstablishmentCode`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdClient`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdClientType`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Month`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaymentType`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RelatedPart`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value01`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value02`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value03`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value04`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value05`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value06`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value07`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value08`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value09`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Value10`** | `numeric(15,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Year`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdTechnicalAnnex01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NumberVoucher`** | `varchar(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TypeEmission`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TypeVoucher`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ClientDescription`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
