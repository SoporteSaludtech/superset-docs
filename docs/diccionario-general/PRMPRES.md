# PRMPRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmCodPre`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrmDscPre`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ParDocCau`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
