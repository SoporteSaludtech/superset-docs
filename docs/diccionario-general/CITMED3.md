# CITMED3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CitEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitConPro`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitProCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitValPro`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitSitPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitTFCscP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitProEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitPrPpal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNumDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCarDie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCnsHis`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFolPrc`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
