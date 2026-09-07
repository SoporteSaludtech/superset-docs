# AUDSERV2

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
| 🔑 | **`AutCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutServ`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AutServCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutServUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutservFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutServObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEstReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
