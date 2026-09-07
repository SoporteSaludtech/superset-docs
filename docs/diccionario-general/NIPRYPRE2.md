# NIPRYPRE2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NiPry2Vig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TpPRub`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TpCapRub`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NiPry2Tip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NiPry2PA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
