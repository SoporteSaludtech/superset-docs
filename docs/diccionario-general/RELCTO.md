# RELCTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CNCCOD`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCCodi`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CnUCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CnUSub`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RelCtoEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
