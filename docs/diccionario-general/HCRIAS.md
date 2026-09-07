# HCRIAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HRIACod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIACtvIn7`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRIADes`** | `char(180)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAFinCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RIAHiCObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAHicEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAHicUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIAActiV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RIATRUT`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
