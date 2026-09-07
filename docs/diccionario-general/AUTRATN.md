# AUTRATN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AutEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MICodI`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ClaPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNroEPS`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutUsrAnl`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDgCli`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCscCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCodPaE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutOrdAmE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNumFaE`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipFaE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCtvInE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipGen`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMedRem`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEspMed`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNomEx`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDgnRln`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutPrdAtn`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutFndSrv`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMddAtn`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutGrpSrv`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTipAtn`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
