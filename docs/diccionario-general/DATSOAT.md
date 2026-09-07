# DATSOAT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DaARP`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNomCto`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaCodOcu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaDesOcu`** | `char(220)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTmpCar`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNitEmp`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNomEmp`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaSitAcc`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaInfAcc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaDFEmp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTipLes`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaParCue`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaAgnAcc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaMecAcc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaLabDes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaComOcu`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaDirEmp`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTelEmp`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaFecAcc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaPrApPr`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaSeApPr`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaPrNoPr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaSeNoPr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTiDoPr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNuDoPr`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaCodDPr`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaCodMPr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaLugExp`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaDirPr`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTelPr`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaPrApCo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaSeApCo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaPrNoCo`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaSeNoCo`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaTipSer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaIntAut`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaCobExc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNumPol`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaFecIniV`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaFecFinV`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatMCDPto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatDocTra`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCscTra`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaCodB`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNRdGlA`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaRadGlo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaNroTFol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DaMedMov`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DATNUMSIR`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DATSERHAB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DATTIPVEH`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
