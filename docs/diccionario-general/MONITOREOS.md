# MONITOREOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TipMonCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TipMonDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UnTpMo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonUltItm`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MONINDAPL`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
