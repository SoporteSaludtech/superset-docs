# LOGSINADO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LogSADCtv`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`LogSADFHo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogSADTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogSADUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogSADEqu`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
