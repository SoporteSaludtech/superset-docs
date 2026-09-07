# SR_SalesCancel01

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CreationDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdDocument`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdOffice`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdTransactionNumber`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TransactionStatus`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Month`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Year`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
