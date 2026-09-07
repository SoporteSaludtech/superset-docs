# EVEGRU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EVEGRUSEC`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EVEGRUDES`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEGRUEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEGRUUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEGRUREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
