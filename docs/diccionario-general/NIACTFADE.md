# NIACTFADE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIACADCNS`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIACADVAD`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADFAA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADFRE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADUAN`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACADFAN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
