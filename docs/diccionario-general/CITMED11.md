# CITMED11

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
| 🔑 | **`CitCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitNaCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitNaFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNaUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNaEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNaObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
