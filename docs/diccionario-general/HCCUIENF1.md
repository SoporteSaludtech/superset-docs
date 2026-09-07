# HCCUIENF1

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
| 🔑 | **`CatCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CuiEnfCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CuiFaRCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CuiFr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiHorIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiEstFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
