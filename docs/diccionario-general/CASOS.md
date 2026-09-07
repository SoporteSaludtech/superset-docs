# CASOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CSCons`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CSDocOri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSTpDocO`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSDocDes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSTpDocD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSDocPpl`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSTpDocP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSTipMod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CSEstAct`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CSOCUFOL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
