# IMARFER

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REFCOD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REfCNSREG`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REFNUNIDE`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`S1CodIma`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REFIMARUT`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFIMAFH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFIMAOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFCODPRO`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REFTIPREG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
