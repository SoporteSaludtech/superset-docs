# DETINT1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocInt`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FolInt`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConDes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FecHorDes`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`DesInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedDes`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipReg`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
