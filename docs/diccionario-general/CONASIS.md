# CONASIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConNro`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCoCe`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCodTrn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConUltCtv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConNroEnt`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
