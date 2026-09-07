# BODEGAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BODDESC`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodPref`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipBodCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCodB`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDirecc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTelefn`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCtrUbi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ClaCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodDspPis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodIntInv`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodCnsg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodComp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodBlqEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodBlqDev`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodUbiCT`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BodTras`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BODINDCM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BODINDPT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BODINDPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodFarExt`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
