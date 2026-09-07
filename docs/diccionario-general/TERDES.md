# TERDES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerDscCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TerDscPor`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerDscAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
