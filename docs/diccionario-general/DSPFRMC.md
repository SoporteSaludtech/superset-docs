# DSPFRMC

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
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DSmCntDsp`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmCntSol`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmUsrReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmCntDes`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmCntDev`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmUltCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsTipDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsTipOri`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCodPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCnsPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCnsSui`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCntUsa`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSSpsErr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSSpsCnf`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSSpsEC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsCodPaq`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSCodEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSConCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSPPPCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSPNroSol`** | `char(35)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmFecSer`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmUsrSer`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DSmEstSer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DsNroPrescMipres`** | `nchar(60)` | SI | Campo transaccional de Hosvital HIS |
