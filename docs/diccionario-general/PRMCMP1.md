# PRMCMP1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TranApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmCodCmp`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrmCmpVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ParCtaEnAl`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
