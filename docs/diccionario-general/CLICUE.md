# CLICUE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CliCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CliCueCXC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLIDCCRE`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLIDCDEB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NICREAC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDEBAC`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
