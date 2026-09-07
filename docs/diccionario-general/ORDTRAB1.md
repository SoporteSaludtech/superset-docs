# ORDTRAB1

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
| 🔑 | **`OrdTrbNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OrdTrbCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaeSerCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbCRb`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbCnt`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrVlrU`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrPrcI`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrDesc`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrCenC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrTotS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrTotI`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrTotD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrEstI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrEstCa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrDocCa`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrFchCa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrInPpt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrPzEn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCCdg`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
