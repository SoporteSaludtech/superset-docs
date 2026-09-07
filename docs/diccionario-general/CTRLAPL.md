# CTRLAPL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrTipCrr`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CtrEstCrr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtrCla`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
