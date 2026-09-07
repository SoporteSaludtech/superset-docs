# CONCEPT11

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConTip`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCod`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCtaVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCtaCXP`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConCtaIna`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConCtaFIna`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCtaUIna`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
