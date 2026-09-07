# DISSRVCC

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
| 🔑 | **`DisSrvCC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DisPrcDis`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`DisIndPto`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
