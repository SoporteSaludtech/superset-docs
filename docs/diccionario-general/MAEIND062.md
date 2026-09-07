# MAEIND062

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IndCodRep`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IndProCod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IndDesRep`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndProDes`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndProPro`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndTipInd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndTotAPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndPrcEda`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndPVeCtr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IndConCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
