# HCCOM512

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
| 🔑 | **`HCAUDIO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRESOTO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODTAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODESTE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODATR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODAGE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODMIC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODMEM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOITAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIESTE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIATR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIAGE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIMIC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIMEM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCNOVOTR`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAYUAUD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIDO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCANTFAM`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCANTPAT`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCHIPOUNI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCHIPOBIL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTINITUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRURITO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOTALGIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAOTRA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPTAOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA3K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA2K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPTAOI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA4K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA3K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPTABIN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA6K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA4K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA250`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA8K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA6K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA500`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA250`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA8K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA1K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA500`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOD99ISO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCODVA2K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOIVA1K`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOI99ISO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPROAGOI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPROAGOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRAGBIN`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCAPAUD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCESPSOL`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMOTREM`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCREPUEST`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRESTULT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOBSERB`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCATE1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCCATE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRESULT1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
