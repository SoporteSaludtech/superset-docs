# NICNANACT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NICNANCOD`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ACTNANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ACTNANNOM`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACTNANDES`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
