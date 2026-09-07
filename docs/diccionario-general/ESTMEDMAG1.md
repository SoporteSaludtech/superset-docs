# ESTMEDMAG1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CEMMCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DEMMCons`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AAMMCod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DEMMLon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DEMMFor`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DEMMParA`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODDIAN`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`POSXML`** | `tinyint` | SI | Campo transaccional de Hosvital HIS |
