# RESFORHC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`codResol`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RFHSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RFHGRU`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RFHORD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFHEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RFHTIP`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESSEGSEC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESPRESEC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
