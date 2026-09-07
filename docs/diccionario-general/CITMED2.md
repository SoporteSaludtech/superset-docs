# CITMED2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CitEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MECodE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`METipMe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitFecMe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitHorIMe`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCanceM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitAsis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
