# NIACTFVUT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIACVUCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIACVUNUE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACVUUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACVUFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACVUMOD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
