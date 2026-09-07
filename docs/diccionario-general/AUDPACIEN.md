# AUDPACIEN

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
| 🔑 | **`AudForCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacFhc`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacUcr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacOto`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPodAud`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPoiAud`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPodLog`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPoiLog`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacObs`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacLau`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacPcu`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacEme`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacEau`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacTco`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacAur`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPacEqu`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudSchOD`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudSchOI`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudSchAte`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudSiste`** | `char(80)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudOido`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudFchAd`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudTiUso`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AudUTiUso`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
