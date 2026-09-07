# CITMED31

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
| 🔑 | **`CitConPro`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitFolPro`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitEstPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CITESTCER`** | `nchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CITNOTACL`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
