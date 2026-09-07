# TURNOSE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TurEsp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CNCCOD`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TurFchVgn`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TurCodTur`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TurDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurHraIni`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurHraFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurEstSCC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
