# MEZCLAS

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
| 🔑 | **`MzcCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MzcDsc`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MzcCntIni`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MzcEst`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
