# ACTDIF1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcDCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcDTACns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcDTANue`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTiAmNu`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTAUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTAFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcDTAFReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
