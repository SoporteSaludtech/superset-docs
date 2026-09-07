# TMPREP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TMPREPID`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TMPREPPRC`** | `varchar(128)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TMPREPDAT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
