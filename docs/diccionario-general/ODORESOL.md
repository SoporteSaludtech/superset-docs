# ODORESOL

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
| 🔑 | **`OdoResCod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OdoResSan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoResNCa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoResCa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoResOCa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoResPCa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoResTDi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
