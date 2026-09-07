# COHORTES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CohoCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CohoMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CohoAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CohoDatos`** | `char(2048)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CohoFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CohoEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
