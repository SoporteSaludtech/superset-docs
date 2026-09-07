# PROCIR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CrgCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CrgPrcCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CrgEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CrgCnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ViaCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesQx`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EspcCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CrgHnrCi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRGPRCAUT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CirFinCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
