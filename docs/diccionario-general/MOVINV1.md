# MOVINV1

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
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtoCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtoCsc1`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtoLot`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtUbiCtv`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoVcto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoCntL`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtLoteES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoNroRq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoFecRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVTOSLDLA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtLEntCn`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtLEntFc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtLEntUs`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
