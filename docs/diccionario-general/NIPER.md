# NIPER

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NIPEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIPANOVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIPMESVIG`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIPTIP`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIPPER`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPUSUCRE`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPFECCRE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPUSUPRO`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPFECPRO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPCEVPOR`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPPEVMES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPPEVTIP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIPPROCAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
