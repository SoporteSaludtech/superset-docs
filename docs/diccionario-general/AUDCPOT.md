# AUDCPOT

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
| 🔑 | **`AucC01Nfo`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudExaCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudGcoCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudCvnCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPotOid`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPotVHz`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPotVdB`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPotFch`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPotUcr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudPotVal`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
