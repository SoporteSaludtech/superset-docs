# ENVHRFDE

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
| 🔑 | **`EnvNroF`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EnvCnsHrf`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EnMcDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnRaCuDo`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnRaCuCn`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnRaReCn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvVaFaF`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvTiPrF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvEsConF`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvDeObF`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvDetObF`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvSedGlo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvGloCtv`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvTipDoc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
