# HEMADUL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMADPCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMADPRC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HEMADPDES`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMADPIMA`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMADPJSO`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMASTXTI`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMADSVG`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
