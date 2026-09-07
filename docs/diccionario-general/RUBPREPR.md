# RUBPREPR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RubPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RubPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RubPreDes`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TpPRub`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TpCapRub`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreDNA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreFCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubPreFMo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RubTipAfe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
