# CAJMEN2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CajMenCod`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConTip`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCod`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CajMenMC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
