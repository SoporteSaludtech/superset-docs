# MOVINV2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtoCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtoCsc2`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtUbiCt1`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoCntNL`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoES1`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTOSLDUA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtUEntCn`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtUEntFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtUEntUs`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
