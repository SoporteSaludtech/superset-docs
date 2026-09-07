# HCOTRDIAG

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
| 🔑 | **`HCODXCOD`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCODXCOAG`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCOTRDXOB`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
