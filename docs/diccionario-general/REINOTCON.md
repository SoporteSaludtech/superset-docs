# REINOTCON

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
| 🔑 | **`REINotCsc`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REINotDes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINotHor`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINotFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINotPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINotFHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
