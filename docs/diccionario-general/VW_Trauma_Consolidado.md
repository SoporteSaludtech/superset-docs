# VW_Trauma_Consolidado

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`Pabellon_Servicio`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Causa_Externa`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CIE10`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Descripcion_Diagnostico`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Sexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ATENCION`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`Id_Paciente`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Grupo_Quinquenal`** | `varchar(5)` | NO | Campo transaccional de Hosvital HIS |
