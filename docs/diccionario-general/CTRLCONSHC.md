# CTRLCONSHC

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
| 🔑 | **`NumDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`UsuSol`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tipsol`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuAut`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecHorSol`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecHorAut`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TiemCons`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstSol`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ObsSol`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MotNeg`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuHabA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecHorHabA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecIniConA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TiemAcConA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
