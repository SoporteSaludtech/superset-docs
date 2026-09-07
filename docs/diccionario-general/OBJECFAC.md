# OBJECFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ObjCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPlaCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjFecTra`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjFacSal`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjValor`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjNumTra`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjEst`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjValSop`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjValAcp`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjUsuCre`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCODNC`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDptoNC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCodNC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NroNotNC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ObjAfeTer`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ObjEstRes`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
