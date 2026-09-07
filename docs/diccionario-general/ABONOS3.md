# ABONOS3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABODOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABONUM`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABOCXCNUM`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABOCXCCON`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ABOFECCXC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOREF`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOVALPAG`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOTO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOSUCCXC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
