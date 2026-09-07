# VW_ESTADISTICAS_TRAUMA

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_DOCUMENTO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOCUMENTO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACIENTE`** | `varchar(121)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ACCIDENTE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SITUACION_ACCIDENTE`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASEGURADORA_SOAT`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
