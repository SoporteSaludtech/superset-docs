# NOTTEC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NotCns`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NotDesc`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotCodCon`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NotFecIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotFecFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotTipFrc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotGenNot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
