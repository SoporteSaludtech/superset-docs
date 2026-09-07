# PPTORES1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocResRef`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocResRNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRefOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRefOcNr`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResObs`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResHorCre`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResHorMod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResEstCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResEstAfec`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResCodAReg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocResSig`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalResDC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRefOcS`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
