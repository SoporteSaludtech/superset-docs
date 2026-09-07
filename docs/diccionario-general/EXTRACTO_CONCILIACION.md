# EXTRACTO_CONCILIACION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MesMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AnioMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`numero_cuenta`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipo_transaccion`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`indicador_dc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`monto`** | `decimal(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`monto_efectivo`** | `decimal(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`monto_cheque`** | `decimal(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`referencia_cliente`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`referencia_banco`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fecha`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`texto_referencia`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fecha_efectiva`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`banco_homologado`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
