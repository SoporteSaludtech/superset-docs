# IMAPRONQ

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
| 🔑 | **`S1CodIma`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IMACNSREG`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImaRutPro`** | `char(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImaFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImaObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMATIPREG`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IMAUSUREG`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
