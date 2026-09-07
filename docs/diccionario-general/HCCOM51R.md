# HCCOM51R

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCConRes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCResulR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUsuRes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFecHRes`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCConclR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFeHReRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDscRAtr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
