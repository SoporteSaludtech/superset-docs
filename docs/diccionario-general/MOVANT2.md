# MOVANT2

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
| 🔑 | **`MvATipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvANroDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOPNoObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCntCon`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCntSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvAFchLeg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAVlrLeg`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAUsrLeg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvAEstLeg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvProLeg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
