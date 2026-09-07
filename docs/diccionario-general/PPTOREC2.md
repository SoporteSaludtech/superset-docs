# PPTOREC2

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
|  | **`SalSitFon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalPolPub`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipNorCod`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalFchNor`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SalNumNor`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
