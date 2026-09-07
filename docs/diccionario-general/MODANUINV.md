# MODANUINV

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
| 🔑 | **`MAICns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAIDocAjs`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAINoDocA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAITipAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAINroNC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAIFecC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
