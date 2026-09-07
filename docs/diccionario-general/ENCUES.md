# ENCUES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EncTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncUlCAg`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncUlCRe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncSexAp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncRaEdI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncTipEdI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncRaEdF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncTipEdF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncTipFol`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncVigIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncVigFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncForObl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ENCORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ENCINDAPL`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncMen`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncAgr`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncTipVer`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
