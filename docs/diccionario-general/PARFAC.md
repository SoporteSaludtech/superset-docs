# PARFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ParFacTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParFacDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacDLo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacRe1`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacRe2`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacFor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParFacPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParTraCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParInvPOS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
