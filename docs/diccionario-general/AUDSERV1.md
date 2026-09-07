# AUDSERV1

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
| 🔑 | **`AutCpt`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutCptVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCptReg`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCptNro`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutCptCpa`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNit`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
