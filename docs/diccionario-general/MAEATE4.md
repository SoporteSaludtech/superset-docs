# MAEATE4

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFcCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ABONUM`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFcFchAbo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFcVlrAbo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFcUsrAbo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaEsPAnuA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboEstCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAAboEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAAboSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAAboDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
