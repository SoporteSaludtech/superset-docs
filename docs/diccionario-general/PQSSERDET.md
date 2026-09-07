# PQSSERDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PQSCNSSER`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PQSCNSDET`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQSTIPSER`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQSCODSER`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQSCNTSER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
