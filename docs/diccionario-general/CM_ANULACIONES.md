# CM_ANULACIONES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`McDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocOriginal`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NumOriginal`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocAnulado`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NumAnulado`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SedeAnulado`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocAjuste`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NumAjuste`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocSoporte`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NumSoporte`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FechaRegistro`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`UsuarioRegistro`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
