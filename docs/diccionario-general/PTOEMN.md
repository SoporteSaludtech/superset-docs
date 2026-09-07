# PTOEMN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PtoEmnCdg`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PtoEmnDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoEmnEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoDocu`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoEmnTip`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
