# VW_Trauma_Prevalencia_Demografia

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`Id_Paciente`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Sexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ATENCION`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tiene_Trauma`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Grupo_Quinquenal`** | `varchar(5)` | NO | Campo transaccional de Hosvital HIS |
