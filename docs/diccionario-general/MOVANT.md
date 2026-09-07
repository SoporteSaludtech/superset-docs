# MOVANT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvAntDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvAntNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvAntCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvAntFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCTESCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCVigTrn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRCCODTRN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntCon`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntDRf`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntSal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAntMCt2`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
