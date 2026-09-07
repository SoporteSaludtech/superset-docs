# TB_EXTERNALCONCEPT01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConceptCode`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConceptDescription`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AccountingType`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdExternalFormat01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
