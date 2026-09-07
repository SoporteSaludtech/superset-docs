# FCTAG02

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFCscP`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFCnsAgr`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AFCntP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVaTP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFPCoSCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFPCoCCs`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFNumOrsP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFTipOrsP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFCscOrsP`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFDatPro`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
