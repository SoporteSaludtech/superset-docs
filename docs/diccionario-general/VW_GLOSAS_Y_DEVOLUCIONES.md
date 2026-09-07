# VW_GLOSAS_Y_DEVOLUCIONES

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`CODIGO_EMPRESA`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_EMPRESA`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_SEDE`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_SEDE`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NUMERO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NUMERO_RADICADO_EPS`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_RADICACION_EPS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TIPO_OBJECION`** | `varchar(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIT_ASEGURADORA`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_ASEGURADORA`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_CONTRATO`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESCRIPCION_CONTRATO`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_PABELLON`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_PABELLON`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CAMA_ATENCION`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONSECUTIVO_GLOSA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_NOTIFICACION_GLOSA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_RESPUESTA_IPS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DIAS_TRAMITE`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ESTADO_GLOSA`** | `varchar(26)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_MOTIVO_GLOSA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_NORMATIVO_GLOSA`** | `varchar(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESCRIPCION_MOTIVO_GLOSA`** | `varchar(500)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_SERVICIO_MEDICAMENTO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESCRIPCION_SERVICIO_MEDICAMENTO`** | `varchar(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CANTIDAD_GLOSADA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_RESPUESTA_IPS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESCRIPCION_RESPUESTA_IPS`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBSERVACION_RESPUESTA`** | `varchar(5000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_GLOSADO`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_ACEPTADO_IPS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_LEVANTADO_IPS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_CONCILIADO`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SALDO_PENDIENTE`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
