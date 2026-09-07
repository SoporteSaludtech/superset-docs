# FIRPREPLU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IdFirman`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FirConse`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FirCargo`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Firmante`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FirFecIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FirFecFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FirNum`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
