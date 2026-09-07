# MAECOTPAG

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
|  | **`CotTipCuo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPorCuo`** | `decimal(9,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValCuo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotFecCuo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCnsUPa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEstCer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
