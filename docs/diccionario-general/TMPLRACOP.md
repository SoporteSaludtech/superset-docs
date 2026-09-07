# TMPLRACOP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TmpLRAEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpLRANro`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpLRADoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpLRAVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpLRACta`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpLRATmo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpLRAFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpLRAObs`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpLRAVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpLRASig`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
