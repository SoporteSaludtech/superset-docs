# MAEMED3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MedFchExc`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MedHoraIni`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MECodE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedHoraFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedMotExc`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedTipExc`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConsCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedTieAte`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedPacMax`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedTipCiI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedTipCiM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedTipCiJ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedPacMaM`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedIncFes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedAgeCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDFECEXC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
