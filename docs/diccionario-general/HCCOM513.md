# HCCOM513

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
| 🔑 | **`HCMOTRIZ`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCACTIEPR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCACNUMER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCACINPUN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCACOBSER`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCACPREAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRMTIEPR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRMNUMER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRMINPUN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRMOBSER`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRMPREAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAVPRDES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAVINPUN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAVOBSER`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAVPREAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCBNUMER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCBTEMER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCBINPUN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCBOBSER`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCBPREAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRFREAFR`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRFINPUN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRFOBSER`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRFPREAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPREG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMESPSOL`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMMOTREM`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMRTA`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMRESTUL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMOBSERB`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMCATE1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMCATE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMRESTUL1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
