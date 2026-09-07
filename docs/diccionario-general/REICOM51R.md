# REICOM51R

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
| 🔑 | **`REICnsRes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIResulR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUsuRes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecHRes`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConcLR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeReRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIC5RPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIC5RFHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
