# DSPFRMC2

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
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSANACON`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DSPCSC`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DSPCANSOL`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
