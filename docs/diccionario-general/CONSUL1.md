# CONSUL1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ConsCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConsDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CoHEntQui`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CoHSalQui`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
