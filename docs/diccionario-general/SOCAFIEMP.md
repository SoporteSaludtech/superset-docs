# SOCAFIEMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`SOcCSec`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcCKey`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcEmpCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcCarCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SOcEmpNom`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCarDes`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcEmpAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcTurno`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcExpTie`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
