# HCNOTCON

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
| 🔑 | **`HCNotCsc`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCNotDes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCNotHor`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCNotFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
