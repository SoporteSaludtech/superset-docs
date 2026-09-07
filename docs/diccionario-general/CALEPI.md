# CALEPI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CalEpiVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CalEpiPer`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CalEpiSem`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CalEpiMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CalEpiDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CalEpiIS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CalEpiFS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
