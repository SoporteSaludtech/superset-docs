# PROGCITAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CitEmpre`** | `varchar(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitCoMedi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitFecha`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitHora`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitCedAsg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTiDocu`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitPacien`** | `varchar(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTele`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNoMedi`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitConsCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNoCons`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitContra`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNomCon`** | `varchar(80)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEstado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitValor`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCoProc`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNoProc`** | `varchar(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTime`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNumCit`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTipCit`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitClaCit`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEspe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitEspeNo`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTiSoli`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAuEmpr`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAuSede`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitDoCons`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAuCons`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitHccTve`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitHisCsE`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCenco`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitProPP`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitProCla`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitSolTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitOriTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitMennit`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAutNro`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAutNom`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAccCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCirNum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitPlaDoc`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitPlaSed`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitPlaEmp`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitMeTipM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
