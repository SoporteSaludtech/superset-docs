# ACFBLTINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFBltNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFBltAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFBltMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFBltFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFBUbiGC`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFBRespC`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFBCCosC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFBUltCn`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFBltEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
