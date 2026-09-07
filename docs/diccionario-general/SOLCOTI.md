# SOLCOTI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SolNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SolFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolFchVto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolUltCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolMsUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdPrc0004`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
