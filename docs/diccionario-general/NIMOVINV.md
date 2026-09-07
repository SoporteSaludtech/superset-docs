# NIMOVINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NIMEMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIMDOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIMDOCNRO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIMMCDPTO`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIMMVTFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMTRACOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMTRAAPL`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMDOCEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMUSUCRE`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMFCHCRE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIMMVTOBS`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
