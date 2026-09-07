# PROCTESO1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCTESCOD`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCCODTRN`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCVigTrn`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrcDscTrn`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcCntTrn`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcFac`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FljCajCon`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FljCajCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcuCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcIndCM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODFOR`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrcCodMPD`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
