# MAEEMP_AUDIT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AuditID`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TableName`** | `nvarchar(256)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OperationType`** | `nvarchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MENNIT`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`OldData`** | `xml` | SI | Campo transaccional de Hosvital HIS |
|  | **`NewData`** | `xml` | SI | Campo transaccional de Hosvital HIS |
|  | **`ChangeDate`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ChangeBy`** | `nvarchar(256)` | SI | Campo transaccional de Hosvital HIS |
