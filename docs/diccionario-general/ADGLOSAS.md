# ADGLOSAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GloFchRec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRec`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTGlo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTAcp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTSop`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTPen`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTAEP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTACo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTCon`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTAcC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrTPCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlTSCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlTACo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchRad`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRad`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumRad`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchNot`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuNot`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoNot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTipReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecDoc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumDoc1`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTipDoc1`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecDoc1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoCoGl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoCoNo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoAfTe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoATe1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoATe2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloConRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloConNot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecConR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecConN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloGenNot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTipCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRNo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumRNo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchRNo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocNCo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchNoC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNroNCo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsrMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocAcC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNroAcC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuAcC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchAcC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVTConc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuNoC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecConC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloCntCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloIndDev`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuNCF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsCNot`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsCCon`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SccEmpG`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCCCodG`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloConDire`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloCnsOrQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUltCoC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUltCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloIndUso`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloIndUsU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPrfGlo`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPrfNot`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPrfCon`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLONUMREM`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLODOCREM`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLOMCDREM`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLOEMPREM`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0008`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADGL_ID`** | `varchar(36)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEstRev`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsrRev`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFecRev`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumRev`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocRev`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0015`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
