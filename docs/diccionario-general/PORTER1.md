# PORTER1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PrTerCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrTerTipAt`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrTerPab`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrTerCon`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrTerExc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTExTpAt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTExPab`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTPabEx`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTerInd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTerPor`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrfCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctoCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForLiqCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTerCnUvr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrterAgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTerEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrAsCd`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTerDAdm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTrSAgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTExCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrTConEx`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
