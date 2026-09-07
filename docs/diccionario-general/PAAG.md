# PAAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PaagAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PaagMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PaagPor`** | `decimal(7,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagAcu`** | `decimal(7,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaagIPC`** | `decimal(7,4)` | SI | Campo transaccional de Hosvital HIS |
