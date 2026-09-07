# CONCUE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCodPag`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConCueIna`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCueFIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCueUIn`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
