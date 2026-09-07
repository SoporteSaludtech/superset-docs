# MAEMED2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgeCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMHorIni`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MECodEAge`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMHorFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMTpoCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMPisCns`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConsCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMTieAte`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMPacMax`** | `numeric(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMTipCiI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMTipCiM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMTipCiJ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMPacMaM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMIncFes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ClaAgeCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMFECMOD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMENCONT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
