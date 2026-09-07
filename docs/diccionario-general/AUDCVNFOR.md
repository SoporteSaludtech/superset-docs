# AUDCVNFOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AudGcoCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudCvnCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CvnForOrd`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CvnForFhc`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`CvnForUcr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudCvnIma`** | `varbinary` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudCvnRim`** | `char(220)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudCnvDco`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudCvnExa`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AudCvnTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
