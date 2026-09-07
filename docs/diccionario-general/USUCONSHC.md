# USUCONSHC

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
| 🔑 | **`UsuConCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`UsuCons`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuHab`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecHorHab`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecIniCon`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TiemAcCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
