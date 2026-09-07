# SMOVTRA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SMTDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SMTCsc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMTTraSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMTTraDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMTTraNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMTSolSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMTSolDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMTSolNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
