# PREXST

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrxCtvo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrxDsc`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Prxfch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrxUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
