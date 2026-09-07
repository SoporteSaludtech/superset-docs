# FACTUR

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
| 🔑 | **`FacturNro`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CLICOD`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturZon`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturUCr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturFeA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturUAn`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturNoC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturTAI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturTDe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturVIm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturDIm`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacturLot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacTotImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacMesFac`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
