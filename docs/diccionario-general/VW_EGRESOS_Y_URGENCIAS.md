# VW_EGRESOS_Y_URGENCIAS

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NUMERO_DOCUMENTO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOCUMENTO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACIENTE`** | `varchar(121)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_INGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_EGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_TOTAL_FACTURA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DIAS_ESTANCIA`** | `int` | SI | Campo transaccional de Hosvital HIS |
