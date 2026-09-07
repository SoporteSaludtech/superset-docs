# RESLEYEPI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLeyDet`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLeyCas`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLeyNEp`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResLeyNumCtr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMes`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMotCie`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyObsMot`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMue`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMueObs`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyRem`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyDiagIni`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyCIE10Ini`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyFinDgn`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyFinCIE10`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyProEgr`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyProObs`** | `varchar(1500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyProDiag`** | `varchar(2000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMedRec`** | `varchar(3000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyProTer`** | `varchar(3000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyComRev`** | `varchar(2500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyMed`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
