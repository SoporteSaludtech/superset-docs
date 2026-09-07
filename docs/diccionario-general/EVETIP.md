# EVETIP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EVEMODEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVEMODSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVETIPSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EVETIPDES`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVETIPEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
