# TERASIS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TerCnta`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerCrgCnt`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipPCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerCupCre`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerPorDes`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerMnjHor`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerAgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerNAutEF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerNAutPar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerUltCns`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerUltHor`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerNroAut`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerFchVen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerAsiExt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
