# CONASIS1

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
| 🔑 | **`ConDCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConCodFPa`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConDocRef`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConBanDoc`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConBanCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTipCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
