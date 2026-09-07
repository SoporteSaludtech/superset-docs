# PACIAIEPI

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
| 🔑 | **`PacMotCon`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DesCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PacAieObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DMCodiCie`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacRies`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
