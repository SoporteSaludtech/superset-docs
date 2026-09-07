# VW_Cronicos_Estructura_Epidemiologica

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`Contrato`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Grupo_Quinquenal`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Sexo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tipo_de_Atencion`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Tipo_Diagnostico`** | `varchar(11)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Clase_Diagnostico`** | `varchar(21)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Sivigila`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Violencia`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Huerfanas`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Infecciosas`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Vectores_ETV`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Transmision_Sexual`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Trauma`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Cronicas`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ATENCION`** | `date` | SI | Campo transaccional de Hosvital HIS |
