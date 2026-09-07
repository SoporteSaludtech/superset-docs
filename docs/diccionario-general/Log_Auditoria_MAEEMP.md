# Log_Auditoria_MAEEMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`LogID`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAEEMP`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IdRegistro`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CampoAlterado`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ValorAnterior`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ValorNuevo`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FechaModificacion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuarioBD`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
