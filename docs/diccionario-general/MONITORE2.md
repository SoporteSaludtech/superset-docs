# MONITORE2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItmCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MonItlCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MonItlVlr`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItlDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonItlAbr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
