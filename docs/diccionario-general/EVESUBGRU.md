# EVESUBGRU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EVEGRUSEC`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVESUBSEC`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EVESUBDES`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVESUBEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVESUBUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVESUBREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
