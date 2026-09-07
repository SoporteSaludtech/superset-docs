# PPTOINTING

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPITipReg`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPIVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPIMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPICntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IPITipVig`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IPIVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IPIEstReg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
