# TB_EXTERNALCONCEPT02

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AccountValidity`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AttributeColumn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`InitialAccountCode`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FinalAccountCode`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BaseTax`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdExternalConcept01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CalculationType`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AccountingType`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
