# AFADIDEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFADCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFAdDVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAdFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAdUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAdFReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAdDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAdNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFADEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
