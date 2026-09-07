# REIRSLPR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrbCod`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRPrCnt`** | `decimal(17,5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRprEnt`** | `decimal(12,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRprTex`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIUnMdCI`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIRPrPa1`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
