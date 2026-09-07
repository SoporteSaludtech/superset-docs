# ENCUES3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncAgrPr`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncItmPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EncItmDsc`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncItmTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncInDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncLonCam`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncOriCam`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncOrdItm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncUlCnCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncCtvRes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncEspAd3`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncMaxLen`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncPlaHol`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncIsReq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncDatTyp`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncPrgMen`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
