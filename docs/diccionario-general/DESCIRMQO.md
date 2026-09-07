# DESCIRMQO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CodEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMcdpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMed`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodCir`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodPrOto`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DesAuAnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuNAnt`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuDAnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuDuAn`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuTpIn`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuSiPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuSPM`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuSPN`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAusPel`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuTQx`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuDTQx`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAudInQx`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInFo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInTa`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCol`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCoDe`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuDLec`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuLech`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuProL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuVPrL`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInEc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInEd`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuMgrC`** | `char(21)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAugrC`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuAde`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuFiD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuDInm`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuFoD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuPosD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuEsP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAutCoc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuMaC`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuInel`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuNumE`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuPosE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuTDi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuLocC`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuObCo`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuObser`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuAna`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCav`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuAsOM`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCOSM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCOSY`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuCOSE`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuLFMT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuEFMT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuRCaC`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuRCoc`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuRFD`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuRCaF`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuObSis`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesAuObMa`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
