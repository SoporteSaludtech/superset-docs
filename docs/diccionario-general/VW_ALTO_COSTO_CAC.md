# VW_ALTO_COSTO_CAC

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
|  | **`CODIGO_COHORTE`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ANIO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_INGRESO_COHORTE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
