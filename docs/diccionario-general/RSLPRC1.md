# RSLPRC1

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
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrbCod`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RPrCnt`** | `decimal(17,5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprEnt`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprText`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UnMdCoIn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprValReI`** | `char(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprUniMeI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprNomUsI`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprDesTeI`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RprCodHom`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
