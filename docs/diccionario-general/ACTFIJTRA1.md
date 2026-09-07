# ACTFIJTRA1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcfNroDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFPriOri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFPriDes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAsigOr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAsigDe`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFFchTra`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SedOriTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SedDesTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UtiOriTr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SUtiOriTr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UtiDesTr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SUtiDesTr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CenOriTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CenDesTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCenOriTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCenDesTr`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FunOriTr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FunDesTr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UbiGeoOri`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UGOriDes`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UbiGeoDes`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFTipTras`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFUsuAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFFchAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFPlaDes`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFPlaOri`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
