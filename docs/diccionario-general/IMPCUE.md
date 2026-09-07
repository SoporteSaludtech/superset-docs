# IMPCUE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IMPCOD`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImpCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImpCntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImpCntAR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpCntIna`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpCntFIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpCntUIn`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpCueARe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
