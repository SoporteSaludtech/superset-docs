# MAECOTI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConse`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConPro`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CotHnrCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotAgrCir`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPorHMe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCODI`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCntPro`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValInP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValToP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUvrVlr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotForLiq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVlrToQ`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotTipQx`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotOpcPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotViaQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEspQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotGruQx`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotTpoTrP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotReCar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCnsQx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotOrdLiq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPtTar`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
