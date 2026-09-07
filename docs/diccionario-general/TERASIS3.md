# TERASIS3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerPrcCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TerPrcFIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerPrcFFn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerPrcDes`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerPrcAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
