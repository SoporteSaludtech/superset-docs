# RESEJE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalCons`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResPreCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VResRef`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`VEjeRef`** | `money` | SI | Campo transaccional de Hosvital HIS |
