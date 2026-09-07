# MAECOTPAD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConse`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotPConse`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotCnsAbo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CotValAbo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEmpAbo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotSedAbo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotDocAbo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotNumAbo`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
