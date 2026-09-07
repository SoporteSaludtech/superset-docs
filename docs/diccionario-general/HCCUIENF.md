# HCCUIENF

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
|  | **`CuiFecIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiUsuRegI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiFecFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiUsuRegF`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiEdo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiNumDias`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiEstFol`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuiObsPla`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
