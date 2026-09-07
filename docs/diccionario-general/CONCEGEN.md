# CONCEGEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CocGenCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CocGenDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConGenTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConGenHom`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GruCocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SubCocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMPCOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
