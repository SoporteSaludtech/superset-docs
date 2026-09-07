# HCCOMRGOX

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCTIPDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPRCSC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFOLREG`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVIAPL`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCHREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCHHIN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCHHFI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCLTRXMN`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTOTLT`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODMDC`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCODEPC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUMECOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVHOFIN`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVHOINI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVHCFIN`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCVHCINI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTIPGAS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
