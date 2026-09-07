# TB_EXTERNALFORMAT01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FormatCode`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FormatConcept`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FormatDescription`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FormatSendingNumber`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FormatVersion`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LesserAmount`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LesserAmountIdThird`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReferenceValue`** | `numeric(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`XmlTag`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Year`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
