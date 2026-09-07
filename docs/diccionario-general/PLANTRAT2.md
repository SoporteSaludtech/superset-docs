# PLANTRAT2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PltCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PltCnsCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PltCnsAct`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PltCodPrD`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PltCntPrD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PltEspPrD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PltTieCiD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
