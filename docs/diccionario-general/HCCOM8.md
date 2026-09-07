# HCCOM8

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
| 🔑 | **`PPPCodA`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PPPAdhCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PPPAdPreg`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PPPAdhCal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
