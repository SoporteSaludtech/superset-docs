# FORLIQ2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForLiqCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HnrCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TopeiSS`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`DsciSS`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctiSS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForCoQxR`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
