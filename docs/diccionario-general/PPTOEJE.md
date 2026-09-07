# PPTOEJE

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
| 🔑 | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalCons`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalPreCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VlrDocRef`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`VlrEjeRef`** | `money` | SI | Campo transaccional de Hosvital HIS |
