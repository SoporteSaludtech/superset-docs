# ABONOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABODOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABONUM`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICOD`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOVLR`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOAPL`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOAPLF`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOSDO`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOCCJ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABODEL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOUSR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOFCS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABODET1`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCTESCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODTRN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurCod`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboCnsUlt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboConta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboEstRei`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboUsrRei`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboFecRei`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboHorRei`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboVlrRei`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboRespNom`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboRespDoc`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboRespTDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboChePost`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboIdPC`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboConAnu`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboFchPost`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNotCre`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNrFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboCtvIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboVlrApr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboCJSCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCVigTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboTipCuo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboOri`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0007`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOFACREC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
