# TRANSFE_HIST

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrsTip`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrsLote`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Contenido`** | `nvarchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FechaCreacion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
