# MONRECANS

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
| 🔑 | **`MonCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RecAnsDsc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorIns`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorInt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorExt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorAns`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonHorTor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonRecEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONCODMED`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonConIn`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonCoASA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonFoli`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonFHUIA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MonEstPac`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONHORECF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONHORECI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECGRA`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECCNA`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECMLO`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECCFL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECMTE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECA0M`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECA5M`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECA1M`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECAFM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECDXP`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECCIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECPOS`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECDER`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECSP`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECACC`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECBOR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECNAI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECNA`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECTA2`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECTPA`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECEQU`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECTA`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECCOA`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECAL`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECBPI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECBP`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECBNI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECBN`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECINT`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECHAB`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECLA`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MONRECASE`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
