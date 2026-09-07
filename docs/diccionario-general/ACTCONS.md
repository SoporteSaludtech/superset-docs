# ACTCONS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ConsCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ActCnsCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ACFchDes`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ACFchHas`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
