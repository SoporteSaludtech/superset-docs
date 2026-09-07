# MOVBAN1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvBNroCmp`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvBCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MVB1ID`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MVB1TRC`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1OPE`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1EST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1VL1`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1VL2`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1F1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1F2`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1CON`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVB1VL3`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVBTRAN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
