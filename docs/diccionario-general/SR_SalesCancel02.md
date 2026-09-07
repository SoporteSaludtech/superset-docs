# SR_SalesCancel02

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TransactionAuthorizationNumber`** | `varchar(49)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionEmissionPoint`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionEndingSequence`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionEstablishment`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionStartingSequence`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionType`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdSalesCancel01`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Month`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Year`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
