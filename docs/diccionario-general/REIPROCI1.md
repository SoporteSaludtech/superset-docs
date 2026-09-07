# REIPROCI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REIEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIPrCiCo`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICrgCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICrgEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ViaCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIMedCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEspCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICrgCnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIDesQx`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICrHnCi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPrcCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
