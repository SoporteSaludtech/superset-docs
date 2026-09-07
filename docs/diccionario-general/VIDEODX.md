# VIDEODX

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
| 🔑 | **`SCodIma`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`VDxRtaArc`** | `char(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VDxFhrArc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`VDxObsArc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SConsecu`** | `int` | NO | Campo transaccional de Hosvital HIS |
