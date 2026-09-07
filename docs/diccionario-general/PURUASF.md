# PURUASF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmCoPrOr`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SeCoPrOr`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PuRuCdOr`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EmCoPrDe`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SeCoPrDe`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PuRuCdDe`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PuRuAsCm`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PuRuAsEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
