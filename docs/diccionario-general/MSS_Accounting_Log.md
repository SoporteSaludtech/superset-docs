# MSS_Accounting_Log

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`idCompany`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idDocument`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idOffice`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idTransactionNumber`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idType`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`idUser`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observation`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`processDate`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
|  | **`idAccounting01`** | `varchar(75)` | SI | Campo transaccional de Hosvital HIS |
