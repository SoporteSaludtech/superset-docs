# ENTRALM1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EntANro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EntACsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntACnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAVlrU`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAVlrI`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAVlrD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAMFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BODEGA`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntATtal`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntATotI`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntEstItm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntDocCau`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntFchCau`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntVUAnt`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntATotD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntUndCmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntFctCnvC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntCntDev`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntOpeTri`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntCntAct`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntSedCau`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntNroCau`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ENTLOTE`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntValOri`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`accept_product`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntNroSer`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntPorImS`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntTotImS`** | `decimal(14,4)` | SI | Campo transaccional de Hosvital HIS |
