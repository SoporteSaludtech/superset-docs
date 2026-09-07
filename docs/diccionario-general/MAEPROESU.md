# MAEPROESU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PRTCOD`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRONESQC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRONDOS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONUNDCD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONVIAPL`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONDIAP`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONFREC`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONFRSM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONFASE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONCNDL`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONDOSMI`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONDOSMA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONDOSSM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONCALIMC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCodiDL`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSPrAcDL`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSFormDL`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CncCdDL`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONCNTDL`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONSUMOB`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONESTSU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONFRH`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRONUNMDL`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRONCONGEN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRONPRCINT`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
