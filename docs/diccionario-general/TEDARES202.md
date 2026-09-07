# TEDARES202

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
| 🔑 | **`EdaRCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EdaRAMG`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EdaRAMF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EdaRAMP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EdaRAMA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EdaRFech`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGEcar`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGEmtb`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
