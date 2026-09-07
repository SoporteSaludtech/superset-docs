# LECRFID

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LecCod`** | `char(120)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LecFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`LecOrdCom`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
