# FORARICO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForAri`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForTopCo`** | `smallmoney` | NO | Campo transaccional de Hosvital HIS |
|  | **`ForDesCo`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForValCo`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForCarCo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
