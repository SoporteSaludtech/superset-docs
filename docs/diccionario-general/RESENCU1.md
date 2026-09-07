# RESENCU1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResDocPac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResTDoPac`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResFolPac`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResCtvRe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResEncCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResTipEnc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResObser`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResVal`** | `decimal(13,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResSele`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResImgJso`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResJsoImg`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResFchHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
