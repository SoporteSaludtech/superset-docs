# HISDGEAC

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
| 🔑 | **`HisGFchAt`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HisGTCEGe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGEcoCo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGEges`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPeso`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTall`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTAD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTAS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGAlUt`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPres`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGMvFet`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGFCF`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGSang`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGInmu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGSngAl`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPrCit`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGFPPa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGInTa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTa1T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTa2T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTa3T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTaPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGInAl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGAl1T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGAl2T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGAl3T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGAlPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGInVi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGVi1T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGVi2T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGVi3T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGViPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGInDr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGDr1T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGDr2T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGDr3T`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGDrPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGExMa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGExOd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPrPa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGCnLac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTrSif`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGEmpCd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGSedAt`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPabAt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGTipAt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGCtvIn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGCnsOC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGPrSan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFAmeno`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISINTGES`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISASE`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISMEDGES`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERINF`** | `varchar(2500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISGESACT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
