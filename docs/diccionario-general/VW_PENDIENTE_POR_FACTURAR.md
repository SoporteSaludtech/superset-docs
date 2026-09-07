# VW_PENDIENTE_POR_FACTURAR

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`CONSECUTIVO_INGRESO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOC_PACIENTE`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IDENTIFICACION_PACIENTE`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACIENTE`** | `char(243)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PABELLON_SERVICIO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_PABELLON`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CAMA_ACTUAL`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_INGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ORDEN_SALIDA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESTADO_ATENCION`** | `varchar(21)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DIAS_REZAGO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RANGO_REZAGO`** | `varchar(11)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RANGO_REZAGO_DETALLADO`** | `varchar(14)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_ATENCION`** | `varchar(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ASEGURADORA`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONTRATO`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESTADO_CONTRATO`** | `varchar(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MODALIDAD_CONTRATO`** | `varchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VALOR_PENDIENTE`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_PROCEDIMIENTOS`** | `decimal(38,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_SUMINISTROS`** | `decimal(38,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CANTIDAD_CARGOS`** | `int` | SI | Campo transaccional de Hosvital HIS |
