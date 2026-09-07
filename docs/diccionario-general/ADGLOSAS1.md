# ADGLOSAS1

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
| 🔑 | **`GlsCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloItem`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloHrioTip`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloItCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GloPrcCtv`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTpoIt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrAcp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrSop`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrAEPS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrConc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrACon`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrAcCo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchRta`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsrRta`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFchrtaN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRtaN`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEdoItm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloedoItNt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocRef1`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocRef2`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocRef3`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlConc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloInATer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObsRec`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObsNot`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloForLiq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrToQ`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTipQx`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloViaQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEspQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloGruQx`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloCnsQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloOpcPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTpoTrp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloRecar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloOrdLiq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPtTar`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloAgrCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUvrVlr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloValTop`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloCntPro`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPorHme`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloValInP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNumOrS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloTidOrS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlSCon`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlACon`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDocNoC`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloRtaNCr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloNotNCr`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObsRes`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloAreGlo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLOCODINT`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLOOBSCOI`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MtvGlsCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`GLOFCAOP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObsRta`** | `varchar(5000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObsCon`** | `varchar(5000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloObConc`** | `varchar(5000)` | SI | Campo transaccional de Hosvital HIS |
