# INACACTF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`InaAFCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`InaAFFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InaAFFac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`InaAFUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InaActUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
