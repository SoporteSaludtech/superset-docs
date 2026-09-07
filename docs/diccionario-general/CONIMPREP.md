# CONIMPREP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConNomRep`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCodCon`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConSalDef`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConNumCop`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
