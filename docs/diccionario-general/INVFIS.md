# INVFIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ID`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvFech`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvTip`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvConcec`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvUsrReg`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvEst`** | `int` | SI | Campo transaccional de Hosvital HIS |
