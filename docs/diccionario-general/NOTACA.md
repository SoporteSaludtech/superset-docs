# NOTACA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NotAcaCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NotAcaDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotAcaTip`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotValCua`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
