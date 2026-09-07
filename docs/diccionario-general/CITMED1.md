# CITMED1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CitEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitNroCto`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFacTpo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEsta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNroAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCance`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecPa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitHorIPa`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitConAcc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitOri`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitExpFHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitExpUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitImpFHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitImpUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCtvIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNumCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitVltPUs`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAutEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAutSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitDocCon`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAutCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNroOrd`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitIndPC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitIndPO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEmpPla`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitSedPla`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitDocPla`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCnsPla`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEspInt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFolInt`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitMedInt`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Citsanped`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Citusulev`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecLev`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecSol`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITEMPC`** | `nchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITSEDC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITDOCNRO`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITDOCCOD`** | `nchar(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITOBSCER`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITNUMPRO`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITMULVLR`** | `numeric(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITABOEMP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITABOSED`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITABODOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITABONUM`** | `numeric(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITDOSCOD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODPROCIT`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitUsrPsC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecPsC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitUsrPrC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecPrC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITSEDCER`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
