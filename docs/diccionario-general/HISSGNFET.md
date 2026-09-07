# HISSGNFET

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
| 🔑 | **`HISFTCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISGNFCF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISGNMVF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISGPRESF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPESFET`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISSITFET`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFETEGES`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
