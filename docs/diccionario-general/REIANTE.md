# REIANTE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIANTIPC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REIANAYUC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIOBANTE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICALANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIANFOHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIANTPAS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
