# REICOM51

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIPrcTpP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrcEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFcHrOr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFcHrAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIResult`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIRPUsRg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConRes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIConI51`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIIntRes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeHInt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFolInt`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMedInt`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDisTri`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstDis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMedDis`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIOrdAmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIUrlIma`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIVerFor`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REISedPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPEsFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPcHrRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINumDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICNumAu`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIInFacC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecReI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFeProI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICodFor`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICnsFac`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICarDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIObsCan`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrUsCaD`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrFhCaD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFcHrPr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAteAgO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIProCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICOM1Pa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFoHC51`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
