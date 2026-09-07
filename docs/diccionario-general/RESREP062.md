# RESREP062

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IndCodRep`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResRepAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResRepPer`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IndProCod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResRepNum`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRepDen`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
