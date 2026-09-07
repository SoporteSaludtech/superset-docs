# SALFLJCAJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalAnioFC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalMesFC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalIniFC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFinFC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFchAct`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalEstFC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
