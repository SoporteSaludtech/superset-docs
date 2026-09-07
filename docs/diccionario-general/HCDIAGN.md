# HCDIAGN

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
| 🔑 | **`HCDXCOD`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCCNSDX`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXCLS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXTIP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXInfNo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDMOtrCo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDMCodAg`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXApto`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDTieEvo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDPreNot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDCauE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDCodDIn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDCodMIn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDCodBIn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDCodPIn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDConSin`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDFchInS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDFchInv`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDFchCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPEDTAG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPEDTAD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXCODEN`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCINDNOTO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXHuefT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXHuefC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDXHueD`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HDXPOSCOR`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
