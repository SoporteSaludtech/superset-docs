# V_FACTURACION_EMITIDA

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_FACTURA`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NUMERO_INGRESO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_DOCUMENTO`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCUMENTO_PACIENTE`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIT_EPS`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_EMPRESA`** | `varchar(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_CONTRATO`** | `varchar(250)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_CONTRATO`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_PABELLON_EGRESO`** | `varchar(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOMBRE_PABELLON_EGRESO`** | `varchar(34)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CODIGO_TIPO_ATENCION`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TIPO_ATENCION`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_INGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_EGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_FACTURACION`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANIO_FACTURACION`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MES_FACTURACION`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PERIODO_FACTURACION`** | `varchar(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANIO_EGRESO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MES_EGRESO`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DIAS_ESTANCIA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DIAS_EGRESO_A_FACTURA`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`RANGO_OPORTUNIDAD`** | `varchar(24)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VALOR_FACTURADO_TOTAL`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VALOR_COPAGO_PACIENTE`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`VALOR_NETO_EPS`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
