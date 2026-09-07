# GN_REPFI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REP_CODI`** | `nvarchar(510)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_PACI`** | `nchar(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_TPAC`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_FECH`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_TIPO`** | `nvarchar(80)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_BLOB`** | `varbinary` | NO | Campo transaccional de Hosvital HIS |
|  | **`REP_INGR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REP_FOLI`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REP_FOLF`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REP_USUA`** | `nchar(20)` | NO | Campo transaccional de Hosvital HIS |
