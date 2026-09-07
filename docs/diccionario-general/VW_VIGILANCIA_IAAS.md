# VW_VIGILANCIA_IAAS

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_DOCUMENTO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOCUMENTO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CONSECUTIVO_INGRESO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CONSECUTIVO_EPIDEMIOLOGIA`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_REGISTRO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FOCO_INFECCIOSO`** | `varchar(2000)` | SI | Campo transaccional de Hosvital HIS |
