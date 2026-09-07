# SOCINFACT

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
|  | **`SOcCaFIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaJor`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaCar`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaSec`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaFun`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaMaq`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaHer`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaMaP`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaTCa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaTSe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaTrO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcCaTrC`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOcObs`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`SOcEmpCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
