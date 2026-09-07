# ENVHR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EnvNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EnvValFac`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvTipPrc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvEstConf`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvDetObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvDetObE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
