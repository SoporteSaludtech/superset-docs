# PAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`SalPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PacMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PacIni`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PacXEje`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PacAdi`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PacCon`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PacSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
