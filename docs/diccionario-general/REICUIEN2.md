# REICUIEN2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CatCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CuiEnfCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CuiFaRCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICuiCtv`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`REICFecAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICUsuAp`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICAplOb`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICAplEd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICFecPr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIEstFo2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICuiPa2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
