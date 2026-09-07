# VW_COHORTES_CAC_LONGITUDINAL

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_DOCUMENTO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOCUMENTO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_COHORTE`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_INDICADOR`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VALOR_INDICADOR`** | `varchar(8000)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_MEDICION`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
