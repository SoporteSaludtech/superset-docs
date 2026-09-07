# ENVHR

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
|  | **`EnvPunRuO`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvPunRuON`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUsuOrg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUsuOrgN`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvFecOri`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvPunRuD`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvPunRuDN`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUsuDes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvUseDesN`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvFecDes`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvEstCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvTipTrn`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvNroOrg`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvCabObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvSedDe`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvConObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnvOrigen`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
