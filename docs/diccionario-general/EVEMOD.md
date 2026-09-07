# EVEMOD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EVEMODEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVEMODSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EVEMODDES`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEMODEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEMODUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEMODREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
