# EVEPROCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EVEPROEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVEPROSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EPCCON`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EPCDES`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EPCEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
