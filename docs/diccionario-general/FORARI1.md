# FORARI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForAri`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ForTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForVlr`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForPrbCod`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForCond`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
